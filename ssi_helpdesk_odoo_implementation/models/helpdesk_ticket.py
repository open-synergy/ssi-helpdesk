# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk_ticket"
    _inherit = [
        "helpdesk_ticket",
    ]

    odoo_implementation_id = fields.Many2one(
        string="# Odoo Implementation",
        comodel_name="odoo_implementation",
    )

    @api.onchange(
        "commercial_partner_id",
    )
    def onchange_odoo_implementation_id(self):
        self.odoo_implementation_id = False
