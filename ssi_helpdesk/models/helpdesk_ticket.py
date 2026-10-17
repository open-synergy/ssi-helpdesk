# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError

from odoo.addons.ssi_decorator import ssi_decorator


class HelpdeskTicket(models.Model):
    """Customer support ticket handled by the helpdesk team.

    Tracks a request from a partner through the draft, confirm, open,
    ready, done, terminate and cancel states, including approval,
    classification, deadline, resolution documentation and the
    communications exchanged with the requester.
    """

    _name = "helpdesk_ticket"
    _inherit = [
        "mixin.transaction_cancel",
        "mixin.transaction_terminate",
        "mixin.transaction_done",
        "mixin.transaction_confirm",
        "mixin.transaction_open",
        "mixin.transaction_ready",
    ]
    _description = "Helpdesk Ticket"

    # Multiple Approval Attribute
    _approval_from_state = "open"
    _approval_to_state = "done"
    _approval_state = "confirm"
    _after_approved_method = "action_done"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True
    _automatically_insert_done_policy_fields = False
    _automatically_insert_done_button = False

    _statusbar_visible_label = "draft,ready,open,confirm,done"

    _policy_field_order = [
        "ready_ok",
        "open_ok",
        "confirm_ok",
        "approve_ok",
        "reject_ok",
        "restart_approval_ok",
        "cancel_ok",
        "terminate_ok",
        "restart_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_ready",
        "action_open",
        "action_confirm",
        "action_approve_approval",
        "action_reject_approval",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "%(ssi_transaction_terminate_mixin.base_select_terminate_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_ready",
        "dom_open",
        "dom_confirm",
        "dom_reject",
        "dom_done",
        "dom_terminate",
        "dom_cancel",
    ]

    _create_sequence_state = "ready"

    title = fields.Char(
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=True,
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
        copy=True,
    )
    commercial_partner_id = fields.Many2one(
        string="Commercial Contact",
        comodel_name="res.partner",
        related=False,
        store=True,
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=True,
    )
    contact_group_ids = fields.Many2many(
        string="Contact Group",
        comodel_name="helpdesk_contact_group",
        relation="rel_helpdesk_ticket_2_contact_group",
        column1="ticket_id",
        column2="group_id",
        copy=True,
    )
    additional_partner_ids = fields.Many2many(
        string="CC To",
        comodel_name="res.partner",
        relation="rel_helpdesk_ticket_2_additional_partner",
        column1="ticket_id",
        column2="partner_id",
        copy=True,
    )
    update_progress = fields.Boolean(
        string="Update Progress",
        default=True,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="helpdesk_type",
        required=False,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=True,
    )
    type_category_id = fields.Many2one(
        string="Category",
        related=False,
        required=False,
        comodel_name="helpdesk_type_category",
        readonly=True,
        states={"draft": [("readonly", False)]},
        copy=True,
    )

    @api.model
    def _default_date(self):
        """Return the default ticket date.

        :return: today's date
        """
        return fields.Date.today()

    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda self: self._default_date(),
        copy=True,
    )
    duration_id = fields.Many2one(
        string="Duration",
        comodel_name="base.duration",
        copy=False,
    )
    date_deadline = fields.Date(
        string="Deadline",
        required=False,
        copy=False,
    )
    description = fields.Html(
        string="Description",
        readonly=False,
        copy=True,
    )
    communication_ids = fields.One2many(
        string="Communications",
        comodel_name="helpdesk_communication",
        inverse_name="ticket_id",
        copy=False,
    )
    starting_communication_id = fields.Many2one(
        string="# Starting Communication",
        comodel_name="helpdesk_communication",
        readonly=True,
        copy=False,
    )
    finishing_communication_id = fields.Many2one(
        string="# Finishing Communication",
        comodel_name="helpdesk_communication",
        readonly=True,
        copy=False,
    )
    latest_message_date = fields.Datetime(
        string="Latest Message Date",
        related="finishing_communication_id.latest_message_date",
        store=True,
        compute_sudo=True,
    )
    latest_partner_message_date = fields.Datetime(
        string="Latest Partner Message Date",
        related="finishing_communication_id.latest_partner_message_date",
        store=True,
        compute_sudo=True,
    )
    finishing_communication_state = fields.Selection(
        string="Finishing Communication State",
        related="finishing_communication_id.state",
        store=True,
        compute_sudo=True,
    )
    duplicate_id = fields.Many2one(
        string="# Duplicate With",
        comodel_name="helpdesk_ticket",
        copy=False,
    )
    duplicate_ids = fields.One2many(
        string="Duplicates",
        comodel_name="helpdesk_ticket",
        inverse_name="duplicate_id",
        copy=False,
    )
    split_id = fields.Many2one(
        string="# Original Ticket",
        comodel_name="helpdesk_ticket",
        copy=False,
    )
    split_ids = fields.One2many(
        string="Split Into",
        comodel_name="helpdesk_ticket",
        inverse_name="split_id",
        copy=False,
    )
    resolution_documentation_ids = fields.One2many(
        string="Resolution Documentations",
        comodel_name="helpdesk_ticket.resolution_documentation",
        inverse_name="ticket_id",
    )
    resolution_documentation_state = fields.Selection(
        string="Resolution Documentation Status",
        selection=[
            ("no_need", "Not Needed"),
            ("open", "In Progress"),
            ("done", "Done"),
        ],
        compute="_compute_resolution_documentation_state",
        store=True,
        compute_sudo=True,
    )
    communication_draft_count = fields.Integer(
        string="Need Respond Count",
        store=True,
        compute="_compute_communication_count",
        compute_sudo=True,
    )
    communication_open_count = fields.Integer(
        string="Waiting for Respond Count",
        store=True,
        compute="_compute_communication_count",
        compute_sudo=True,
    )

    @api.onchange("commercial_partner_id")
    def onchange_partner_id(self):
        self.partner_id = False

    @api.model
    def _get_policy_field(self):
        res = super()._get_policy_field()
        policy_field = [
            "ready_ok",
            "open_ok",
            "confirm_ok",
            "approve_ok",
            "reject_ok",
            "restart_approval_ok",
            "done_ok",
            "cancel_ok",
            "restart_ok",
            "terminate_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @api.depends(
        "resolution_documentation_ids",
        "resolution_documentation_ids.state",
    )
    def _compute_resolution_documentation_state(self):
        """Compute the state of the resolution documentation.

        ``no_need`` when no documentation is required, ``open`` when at
        least one required documentation is still open, otherwise
        ``done``.
        """
        for record in self:
            result = "no_need"

            count_req = len(record.resolution_documentation_ids)

            if count_req > 0:
                result = "done"
                for req in record.resolution_documentation_ids:
                    if req.state == "open":
                        result = "open"

            record.resolution_documentation_state = result

    @api.onchange(
        "partner_id",
        "contact_group_ids",
    )
    def onchange_additional_partner_ids(self):
        """Recompute the CC contacts from the selected contact groups.

        Collects the contacts of all selected contact groups, leaves
        out the ticket contact and stores the rest in
        ``additional_partner_ids``. Without groups the field is
        emptied.
        """
        self.additional_partner_ids = [(6, 0, [])]

        if self.contact_group_ids:
            contact_groups = self.contact_group_ids.mapped("contact_ids")
            # TODO: This is not working. Why?
            contact_groups = contact_groups - self.partner_id
            self.additional_partner_ids = [(6, 0, contact_groups.ids)]

    @api.onchange(
        "type_category_id",
    )
    def onchange_type_id(self):
        self.type_id = False

    @api.onchange(
        "type_id",
    )
    def onchange_title(self):
        result = ""
        if self.type_id and self.type_category_id.auto_title:
            result = "%s - %s" % (self.type_category_id.name, self.type_id.name)
        self.title = result

    @api.onchange(
        "partner_id",
    )
    def onchange_contact_group_ids(self):
        self.contact_group_ids = [(6, 0, [])]

    @api.onchange(
        "type_id",
    )
    def onchange_duration_id(self):
        self.duration_id = False
        if self.type_id:
            self.duration_id = self.type_id.duration_id

    @api.onchange(
        "duration_id",
        "date",
    )
    def onchange_date_deadline(self):
        """Recompute the deadline from the selected duration.

        The deadline is the ticket date moved forward by the duration.
        Without a duration the deadline is emptied.
        """
        self.date_deadline = False
        if self.duration_id:
            self.date_deadline = self.duration_id.get_duration(self.date)

    @api.model_create_multi
    def create(self, values):
        """Create tickets and generate their sequence.

        Overridden so that every new ticket gets its number from the
        sequence template applicable to it.

        :param values: list of ``helpdesk_ticket`` value dicts
        :return: the created ``helpdesk_ticket`` recordset
        """
        _super = super()
        results = _super.create(values)
        for result in results:
            result._create_sequence()
        return result

    def action_create_finishing_communication(self):
        """Create the finishing communication for the ticket.

        Runs ``_create_finishing_communication`` on each ticket.

        :return: ``ir.actions.act_window`` dict opening the new
            communication form
        """
        for record in self.sudo():
            result = record._create_finishing_communication()
        return result

    def action_create_updating_communication(self):
        """Create a status update communication for the ticket.

        Runs ``_create_updating_communication`` on each ticket.

        :return: ``ir.actions.act_window`` dict opening the new
            communication form
        """
        for record in self.sudo():
            result = record._create_updating_communication()
        return result

    def action_open_communication(self):
        """Open the communications linked to the ticket.

        Runs ``_open_communication`` on each ticket.

        :return: ``ir.actions.act_window`` dict listing the ticket
            communications
        """
        for record in self.sudo():
            result = record._open_communication()
        return result

    def action_open_split(self):
        """Open the tickets split from this ticket.

        :return: window action listing the child tickets
        """
        for record in self.sudo():
            result = record._open_split()
        return result

    def _open_split(self):
        """Build the window action listing tickets split from this one.

        The action context defaults ``split_id`` to this ticket so new
        child tickets are linked to it.

        :return: window action dict
        """
        waction = self.env.ref("ssi_helpdesk.helpdesk_ticket_action").read()[0]
        new_context = {
            "default_split_id": self.id,
        }
        waction.update(
            {
                "view_mode": "tree,form",
                "domain": [("split_id", "=", self.id)],
                "context": new_context,
            }
        )
        return waction

    def _open_communication(self):
        """Build the window action listing the ticket communications.

        The domain is restricted to ``helpdesk_communication`` records
        whose ``ticket_id`` is this ticket.

        :return: ``ir.actions.act_window`` dict in tree and form mode
        """
        waction = self.env.ref("ssi_helpdesk.helpdesk_communication_action").read()[0]
        waction.update(
            {
                "view_mode": "tree,form",
                "domain": [("ticket_id", "=", self.id)],
            }
        )
        return waction

    def _create_finishing_communication(self):
        """Create the finishing communication and link it to the ticket.

        Subscribes the ticket partner and the additional partners to
        the new communication, then stores it in
        ``finishing_communication_id``.

        :return: ``ir.actions.act_window`` dict opening the new
            communication form
        """
        HC = self.env["helpdesk_communication"]
        hc = HC.create(self._prepare_create_finishing_communication())
        partner_ids = (self.additional_partner_ids + self.partner_id).ids
        hc.message_subscribe(partner_ids)
        self.write(
            {
                "finishing_communication_id": hc.id,
            }
        )
        return {
            "name": hc.title,
            "view_mode": "form",
            "res_model": "helpdesk_communication",
            "res_id": hc.id,
            "type": "ir.actions.act_window",
        }

    def _create_updating_communication(self):
        """Create a status update communication for the ticket.

        Subscribes the ticket partner and the additional partners to
        the new communication. Unlike the finishing communication, it
        is not stored on the ticket.

        :return: ``ir.actions.act_window`` dict opening the new
            communication form
        """
        self.ensure_one()
        HC = self.env["helpdesk_communication"]
        hc = HC.create(self._prepare_create_updating_communication())
        partner_ids = (self.additional_partner_ids + self.partner_id).ids
        hc.message_subscribe(partner_ids)
        return {
            "name": hc.title,
            "view_mode": "form",
            "res_model": "helpdesk_communication",
            "res_id": hc.id,
            "type": "ir.actions.act_window",
        }

    def _prepare_create_finishing_communication(self):
        """Build the values of the finishing communication.

        Extension point: override in a glue module to add values
        before ``_create_finishing_communication`` creates the record.

        :return: dict of ``helpdesk_communication`` values
        """
        return {
            "partner_id": self.partner_id.id,
            "title": self.title,
            "ticket_id": self.id,
        }

    def _prepare_create_updating_communication(self):
        """Build the values of the status update communication.

        The title combines the ticket name and today's date. Extension
        point: override in a glue module to add values.

        :return: dict of ``helpdesk_communication`` values
        """
        title = "Ticket status update - %s - %s" % (self.name, fields.Date.today())
        return {
            "partner_id": self.partner_id.id,
            "title": title,
            "ticket_id": self.id,
        }

    @api.depends("communication_ids", "communication_ids.state")
    def _compute_communication_count(self):
        """Compute the communication counters of the ticket.

        Fill ``communication_draft_count`` with the communications in
        ``draft`` state and ``communication_open_count`` with those in
        ``open`` state.
        """
        for record in self:
            record.communication_draft_count = len(
                record.communication_ids.filtered(lambda x: x.state == "draft")
            )
            record.communication_open_count = len(
                record.communication_ids.filtered(lambda x: x.state == "open")
            )

    @ssi_decorator.insert_on_form_view()
    def _insert_form_element(self, view_arch):
        if self._automatically_insert_view_element:
            view_arch = self._reconfigure_statusbar_visible(view_arch)
        return view_arch

    @ssi_decorator.pre_confirm_check()
    def _10_check_split_tickets_finished_on_confirm(self):
        """Block confirmation while split tickets are unfinished.

        :raises UserError: if a ticket split from this one is neither
            done, cancelled nor terminated
        """
        self.ensure_one()
        self._check_split_tickets_finished("Confirm Ticket")

    @ssi_decorator.pre_done_check()
    def _10_check_split_tickets_finished_on_done(self):
        """Block completion while split tickets are unfinished.

        :raises UserError: if a ticket split from this one is neither
            done, cancelled nor terminated
        """
        self.ensure_one()
        self._check_split_tickets_finished("Finish Ticket")

    def _check_split_tickets_finished(self, context):
        """Ensure every ticket split from this one has been settled.

        A split ticket is settled when its state is ``done``,
        ``cancel`` or ``terminate``.

        :param str context: operation name shown in the error message
        :raises UserError: listing the split tickets still in progress
        """
        self.ensure_one()
        unfinished = self.split_ids.filtered(
            lambda x: x.state not in ("done", "cancel", "terminate")
        )
        if unfinished:
            error_message = _(
                """
Context: %s
Database ID: %s
Problem: Tickets split from this ticket are not finished yet: %s
Solution: Finish, cancel or terminate the split tickets first
"""
                % (
                    context,
                    self.id,
                    ", ".join("%s [%s]" % (x.name, x.title) for x in unfinished),
                )
            )
            raise UserError(error_message)
