# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HelpdeskType(models.Model):
    _name = "helpdesk_type"
    _inherit = [
        "helpdesk_type",
    ]

    need_task = fields.Boolean(
        string="Need Task",
        default=False,
    )
