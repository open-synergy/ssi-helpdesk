# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class SplitHelpdeskTicket(models.TransientModel):
    _name = "split_helpdesk_ticket"
    _inherit = "split_helpdesk_ticket"

    def _run_ticket_onchange(self):
        """Run the need-task onchange on the resulting ticket.

        Extends the base implementation so that the ticket created by
        the split gets its task-related defaults.
        """
        self.ensure_one()
        _super = super(SplitHelpdeskTicket, self)
        _super._run_ticket_onchange()
        self.result_ticket_id.onchange_need_task()
