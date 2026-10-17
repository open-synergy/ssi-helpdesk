# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SplitHelpdeskTicket(models.TransientModel):
    """Collect the input needed to split a helpdesk ticket.

    The wizard copies the source ticket into a new one with its own
    title, category, type and description, and links the two tickets.
    """

    _name = "split_helpdesk_ticket"
    _description = "Split Helpdesk Ticket"

    @api.model
    def _default_ticket_id(self):
        """Return the ticket this wizard was opened from.

        :return: ``helpdesk_ticket`` id from ``active_id``, or ``False``
        """
        return self.env.context.get("active_id", False)

    ticket_id = fields.Many2one(
        string="# Ticket",
        comodel_name="helpdesk_ticket",
        required=True,
        default=lambda self: self._default_ticket_id(),
    )
    result_ticket_id = fields.Many2one(
        string="# Split result",
        comodel_name="helpdesk_ticket",
    )
    title = fields.Char(
        string="Title",
        required=True,
    )
    description = fields.Html(
        string="Description",
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
        """Split the ticket and open the resulting one.

        :return: an ``ir.actions.act_window`` dict for the new ticket
        """
        for record in self.sudo():
            result = record._split_ticket()
        return result

    def _run_ticket_onchange(self):
        """Recompute the duration and deadline of the split result.

        Side effect: runs the ticket onchange methods on the result.
        """
        self.ensure_one()
        self.result_ticket_id.onchange_duration_id()
        self.result_ticket_id.onchange_date_deadline()

    def _prepare_split_values(self):
        """Build the values used to copy the source ticket.

        Extension point: override in a glue module to add more values.

        :return: dict of ``helpdesk_ticket`` values
        """
        self.ensure_one()
        return {
            "title": self.title,
            "split_id": self.ticket_id.id,
            "type_category_id": self.category_id.id,
            "type_id": self.type_id.id,
            "description": self.description,
        }

    def _split_ticket(self):
        """Copy the source ticket into a new one and link them.

        Side effect: writes the new ticket on ``result_ticket_id``.

        :return: an ``ir.actions.act_window`` dict for the new ticket
        """
        self.ensure_one()
        ticket = self.ticket_id.copy(default=self._prepare_split_values())
        self.write(
            {
                "result_ticket_id": ticket.id,
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
