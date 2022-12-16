# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk_ticket"
    _inherit = [
        "mixin.transaction_open",
        "mixin.transaction_done",
        "mixin.transaction_cancel",
        "mixin.transaction_terminate",
    ]
    _description = "Helpdesk Ticket"
    _approval_from_state = "draft"

    # Attributes related to add element on view automatically
    _automatically_insert_view_element = True

    _statusbar_visible_label = "draft,open,done"

    _policy_field_order = [
        "open_ok",
        "restart_approval_ok",
        "cancel_ok",
        "terminate_ok",
        "restart_ok",
        "done_ok",
        "manual_number_ok",
    ]
    _header_button_order = [
        "action_open",
        "action_done",
        "%(ssi_transaction_cancel_mixin.base_select_cancel_reason_action)d",
        "%(ssi_transaction_terminate_mixin.base_select_terminate_reason_action)d",
        "action_restart",
    ]

    # Attributes related to add element on search view automatically
    _state_filter_order = [
        "dom_draft",
        "dom_open",
        "dom_done",
        "dom_terminate",
        "dom_cancel",
    ]

    _create_sequence_state = "open"

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
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="helpdesk_type",
        required=False,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    type_category_id = fields.Many2one(
        string="Category",
        related="type_id.category_id",
        store=True,
    )

    @api.model
    def _default_date(self):
        return fields.Date.today()

    date = fields.Date(
        string="Date",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda self: self._default_date(),
    )
    description = fields.Html(
        string="Description",
        readonly=False,
    )
    communication_ids = fields.One2many(
        string="Communications",
        comodel_name="helpdesk_communication",
        inverse_name="ticket_id",
    )
    starting_communication_id = fields.Many2one(
        string="# Starting Communication",
        comodel_name="helpdesk_communication",
        readonly=True,
    )
    finishing_communication_id = fields.Many2one(
        string="# Finishing Communication",
        comodel_name="helpdesk_communication",
        readonly=True,
    )
    finishing_communication_state = fields.Selection(
        string="Finishing Communication State",
        related="finishing_communication_id.state",
        store=True,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("open", "In Progress"),
            ("done", "Done"),
            ("terminate", "Terminate"),
            ("cancel", "Cancelled"),
        ],
        copy=False,
        default="draft",
        required=True,
        readonly=True,
    )

    @api.model
    def _get_policy_field(self):
        res = super(HelpdeskTicket, self)._get_policy_field()
        policy_field = [
            "open_ok",
            "done_ok",
            "cancel_ok",
            "restart_ok",
            "terminate_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    def action_create_finishing_communication(self):
        for record in self.sudo():
            record._create_finishing_communication()

    def _create_finishing_communication(self):
        HC = self.env["helpdesk_communication"]
        hc = HC.create(self._prepare_create_finishing_communication())
        self.write(
            {
                "finishing_communication_id": hc.id,
            }
        )

    def _prepare_create_finishing_communication(self):
        return {
            "partner_id": self.partner_id.id,
            "title": self.title,
            "ticket_id": self.id,
        }
