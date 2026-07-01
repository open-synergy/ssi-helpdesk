# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import api, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk_ticket"
    _inherit = [
        "helpdesk_ticket",
    ]

    @api.onchange(
        "odoo_implementation_id",
    )
    def onchange_project_id(self):
        self.project_id = False
        if self.odoo_implementation_id and self.odoo_implementation_id.project_id:
            self.project_id = self.odoo_implementation_id.project_id
