# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CreateTicketFromCommunication(models.TransientModel):
    """Create a helpdesk ticket from a communication.

    The wizard collects the ticket category and type, creates the
    ticket and links it back to the originating communication.
    """

    _name = "create_ticket_from_communication"
    _description = "Create Ticket From Communication"

    @api.model
    def _default_communication_id(self):
        """Return the communication the wizard was opened from.

        :return: ``helpdesk_communication`` id, or ``False``
        """
        return self.env.context.get("active_id", False)

    communication_id = fields.Many2one(
        string="# Communication",
        comodel_name="helpdesk_communication",
        required=True,
        default=lambda self: self._default_communication_id(),
    )
    category_id = fields.Many2one(
        string="Category",
        comodel_name="helpdesk_type_category",
        required=True,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="helpdesk_type",
        required=True,
    )

    @api.onchange(
        "category_id",
    )
    def onchange_type_id(self):
        self.type_id = False

    def action_confirm(self):
        """Create the ticket and open it.

        :return: an ``ir.actions.act_window`` dict for the new ticket
        """
        for record in self.sudo():
            result = record._create_ticket()
        return result

    def _run_ticket_onchange(self):
        """Run the ticket onchange methods on the linked ticket.

        Side effect: recomputes duration and deadline on the ticket.
        """
        self.ensure_one()
        self.communication_id.ticket_id.onchange_duration_id()
        self.communication_id.ticket_id.onchange_date_deadline()

    def _create_ticket(self):
        """Create the ticket and link it to the communication.

        Side effect: writes ``ticket_id`` on the communication.

        :return: an ``ir.actions.act_window`` dict for the new ticket
        """
        self.ensure_one()
        Ticket = self.env["helpdesk_ticket"]
        ticket = Ticket.create(self._prepare_create_ticket())
        self.communication_id.write(
            {
                "ticket_id": ticket.id,
            }
        )
        self._run_ticket_onchange()
        return {
            "name": ticket.title,
            "view_mode": "form",
            "res_model": "helpdesk_ticket",
            "res_id": ticket.id,
            "type": "ir.actions.act_window",
        }

    def _prepare_create_ticket(self):
        """Prepare the values used to create the ticket.

        :return: dict of ``helpdesk_ticket`` create values
        """
        self.ensure_one()
        communication = self.communication_id
        return {
            "partner_id": communication.partner_id.id,
            "commercial_partner_id": communication.commercial_partner_id.id,
            "type_id": self.type_id.id,
            "type_category_id": self.category_id.id,
            "date": communication.date,
            "title": communication.title,
            "starting_communication_id": communication.id,
        }
