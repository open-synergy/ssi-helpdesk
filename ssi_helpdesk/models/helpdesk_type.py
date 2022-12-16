# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HelpdeskType(models.Model):
    _name = "helpdesk_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Helpdesk Type"

    category_id = fields.Many2one(
        string="Category",
        comodel_name="helpdesk_type_category",
    )
