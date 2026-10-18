# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import SUPERUSER_ID, _, api, fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class HelpdeskCommunication(models.Model):
    """Records a communication exchanged with a customer contact.

    A communication is a lightweight document (draft, open, done) that
    can be linked to a helpdesk ticket. It keeps the latest company and
    partner messages to show whether a response is still awaited.
    """

    _name = "helpdesk_communication"
    _inherit = [
        "mixin.transaction_done",
        "mixin.transaction_open",
    ]
    _description = "Helpdesk Communication"
    _approval_from_state = "draft"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True

    _statusbar_visible_label = "draft,open,done"

    _policy_field_order = [
        "open_ok",
        "restart_approval_ok",
        "restart_ok",
        "done_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_open",
        "action_done",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_open",
        "dom_done",
    ]

    _create_sequence_state = False

    title = fields.Char(
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    partner_id = fields.Many2one(
        string="Contact",
        comodel_name="res.partner",
        domain=[
            ("is_company", "=", False),
            ("parent_id", "!=", False),
        ],
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    commercial_partner_id = fields.Many2one(
        string="Commercial Contact",
        comodel_name="res.partner",
        related="partner_id.commercial_partner_id",
        store=True,
        compute_sudo=True,
    )
    ticket_id = fields.Many2one(
        string="# Ticket",
        comodel_name="helpdesk_ticket",
        ondelete="restrict",
    )

    @api.depends(
        "message_ids",
    )
    def _compute_need_respon(self):
        """Compute the latest messages and the waiting-for-response flag.

        The three stored fields are computed together, from local
        variables, so the ``base.automation`` rules that read
        ``need_respon`` never see a value derived from stale sources.

        Among the email and comment messages, ``latest_message_id`` is
        the newest one written by the company partner and
        ``latest_partner_message_id`` is the newest one written by
        anybody else. ``need_respon`` is True when only a company
        message exists, or when the company message is newer than the
        partner message. Otherwise it is False.
        """
        for record in self:
            company_partner_id = record.company_id.partner_id.id
            messages = record.message_ids.filtered(
                lambda r: r.message_type in ["email", "comment"]
            ).sorted("id", reverse=True)
            company_messages = messages.filtered(
                lambda r: r.author_id.commercial_partner_id.id == company_partner_id
            )
            company_message = company_messages[:1]
            partner_message = (messages - company_messages)[:1]

            result = False
            if company_message and not partner_message:
                result = True
            elif company_message and partner_message:
                result = company_message.id > partner_message.id

            record.latest_message_id = company_message
            record.latest_partner_message_id = partner_message
            record.need_respon = result

    latest_message_id = fields.Many2one(
        string="Latest Message",
        comodel_name="mail.message",
        readonly=True,
        compute="_compute_need_respon",
        store=True,
        compute_sudo=True,
    )
    latest_message_date = fields.Datetime(
        string="Latest Message Date",
        related="latest_message_id.date",
        store=True,
        compute_sudo=True,
    )
    latest_partner_message_id = fields.Many2one(
        string="Latest Partner Message",
        comodel_name="mail.message",
        readonly=True,
        compute="_compute_need_respon",
        store=True,
        compute_sudo=True,
    )
    latest_partner_message_date = fields.Datetime(
        string="Latest Partner Message Date",
        related="latest_partner_message_id.date",
        store=True,
        compute_sudo=True,
    )
    need_respon = fields.Boolean(
        string="Waiting for Respon",
        compute="_compute_need_respon",
        store=True,
        compute_sudo=True,
    )

    @api.model
    def _default_date(self):
        """Return the default communication date.

        :return: today's date
        """
        return fields.Date.today()

    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda self: self._default_date(),
    )
    channel_id = fields.Many2one(
        string="Channel",
        comodel_name="helpdesk_channel",
        required=False,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    description = fields.Html(
        string="Description",
        readonly=False,
    )

    @api.model_create_multi
    def create(self, values):
        """Create communications and generate their document numbers.

        Overridden because the sequence is created explicitly through
        ``_create_sequence`` instead of by the state transition.

        :param values: list of dicts of field values
        :return: the created communication records
        """
        _super = super()
        results = _super.create(values)
        for result in results:
            result._create_sequence()
        return result

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        """Overrides mail_thread message_new that is called by the mailgateway
        through message_process.
        This override updates the document according to the email.
        """
        # remove external users
        if self.env.user.has_group("base.group_portal"):
            self = self.with_context(default_user_id=False)

        # remove default author when going through the mail gateway. Indeed we
        # do not want to explicitly set user_id to False; however we do not
        # want the gateway user to be responsible if no other responsible is
        # found.
        if self._uid == self.env.ref("base.user_root").id:
            self = self.with_context(default_user_id=False)

        if custom_values is None:
            custom_values = {}
        defaults = {
            "name": "/",
            "title": msg_dict.get("subject") or _("No Subject"),
            "date": fields.Date.today(),
            "partner_id": msg_dict.get("author_id"),
            "user_id": SUPERUSER_ID,
            "description": msg_dict.get("body") or "-",
        }
        defaults.update(custom_values)
        return super().message_new(msg_dict, custom_values=defaults)

    # @api.model
    # def message_new(self, msg, custom_values=None):
    #     create_context = dict(self.env.context or {})
    #     create_context["default_user_id"] = False
    #     if custom_values is None:
    #         custom_values = {}
    #     defaults = {
    #         "name": "/",
    #         "title": msg.get("subject") or _("No Subject"),
    #         "date": fields.Date.today(),
    #         "partner_id": msg.get("author_id"),
    #         "user_id": SUPERUSER_ID,
    #         "description": msg.get("body") or "-",
    #     }
    #     defaults.update(custom_values)
    #
    #     helpdeks_communication = super(
    #         HelpdeskCommunication, self.with_context(create_context)
    #     ).message_new(msg, custom_values=defaults)
    #     email_list = helpdeks_communication.email_split(msg)
    #     partner_ids = [
    #         p.id
    #         for p in self.env["mail.thread"]._mail_find_partner_from_emails(
    #             email_list, records=helpdeks_communication, force_create=False
    #         )
    #         if p
    #     ]
    #     customer_ids = [
    #         p.id
    #         for p in self.env["mail.thread"]._mail_find_partner_from_emails(
    #             tools.email_split(defaults["email_from"]),
    #             records=helpdeks_communication,
    #         )
    #         if p
    #     ]
    #     partner_ids += customer_ids
    #     helpdeks_communication.message_subscribe(partner_ids)
    #     attachment_ids = []
    #     for attachment in msg.get("attachments", []):
    #         file_name = attachment[0]
    #         file = attachment[1]
    #         attachment_id = (
    #             self.env["ir.attachment"]
    #             .sudo()
    #             .create(
    #                 {
    #                     "name": file_name,
    #                     "type": "binary",
    #                     "datas": base64.b64encode(file),
    #                     "res_model": helpdeks_communication._name,
    #                     "res_id": helpdeks_communication.id,
    #                 }
    #             )
    #         )
    #         attachment_ids.append(attachment_id.id)
    #     if attachment_ids:
    #         helpdeks_communication.message_post(attachment_ids=attachment_ids)
    #     return helpdeks_communication

    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "open_ok",
            "done_ok",
            "restart_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    def action_reload_followers(self):
        """Subscribe the ticket contacts as followers of the communication.

        For every communication linked to a ticket, subscribe the ticket
        responsible user, the ticket contact and the ticket additional
        partners (CC To). Communications without a ticket are skipped.
        """
        for rec in self:
            if not rec.ticket_id:
                continue
            partner_ids = rec.message_partner_ids
            partner_ids |= (
                rec.ticket_id.user_id.partner_id
                + rec.ticket_id.partner_id
                + rec.ticket_id.additional_partner_ids
            )
            rec.message_subscribe(partner_ids.ids)

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch
