# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class HelpdeskTicketForceClose(models.TransientModel):
    """Collect the reason to force close a helpdesk ticket.

    Force closing records who bypassed the resolution documentation
    gate and why. The ticket then runs the normal confirm, approval and
    done flow.
    """

    _name = "helpdesk_ticket_force_close"
    _description = "Helpdesk Ticket Force Close"

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
    reason = fields.Text(
        string="Reason",
        required=True,
    )

    def action_confirm(self):
        """Force close the ticket with the given reason.

        :return: ``ir.actions.act_window_close`` dict
        :raises UserError: if the active user is not allowed by the
            ``force_close_ok`` policy
        """
        for record in self:
            record._force_close_ticket()
        return {"type": "ir.actions.act_window_close"}

    def _force_close_ticket(self):
        """Write the reason and the user on the ticket.

        Side effect: fills ``force_close_reason`` and
        ``force_close_user_id`` of the ticket.

        :raises UserError: if the reason is blank or the policy denies
            force close
        """
        self.ensure_one()
        ticket = self.ticket_id
        if not (self.reason or "").strip():
            error_message = _(
                """
Context: Force Close Ticket
Database ID: %s
Problem: Force close reason is empty
Solution: Fill in the reason to force close the ticket
"""
                % ticket.id
            )
            raise UserError(error_message)
        if not ticket.force_close_ok:
            error_message = _(
                """
Context: Force Close Ticket
Database ID: %s
Problem: Force close is not allowed
Solution: Check the force close policy prerequisite
"""
                % ticket.id
            )
            raise UserError(error_message)
        ticket.write(
            {
                "force_close_reason": self.reason,
                "force_close_user_id": self.env.user.id,
            }
        )
