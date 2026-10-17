# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicketDataRequirement(models.Model):
    """Data requirement line of a helpdesk ticket.

    Records one piece of data the requester must provide for the
    ticket, optionally typed, with a URL or attachment and the date it
    was submitted.
    """

    _name = "helpdesk_ticket.data_requirement"
    _description = "Helpdesk Ticket Data Requirement"
    _order = "ticket_id, sequence, id"

    ticket_id = fields.Many2one(
        string="# Helpdesk Ticket",
        comodel_name="helpdesk_ticket",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=10,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="helpdesk_data_requirement_type",
        ondelete="restrict",
    )
    name = fields.Char(
        string="Requirement",
        required=True,
    )
    url = fields.Char(
        string="URL",
    )
    attachment_id = fields.Many2one(
        string="Attachment",
        comodel_name="ir.attachment",
        ondelete="restrict",
    )
    date_submit = fields.Date(
        string="Date Submit",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("open", "In Progress"),
            ("done", "Done"),
        ],
        compute="_compute_state",
        store=True,
        compute_sudo=True,
    )

    @api.depends(
        "date_submit",
    )
    def _compute_state(self):
        """Compute the state of the requirement.

        The state is ``done`` once the submit date is filled, otherwise
        ``open``.
        """
        for record in self:
            result = "open"
            if record.date_submit:
                result = "done"
            record.state = result

    @api.onchange(
        "type_id",
    )
    def onchange_name(self):
        """Fill the requirement name from the selected type.

        The name is the type name, or empty when no type is selected.
        """
        self.name = False
        if self.type_id:
            self.name = self.type_id.name
