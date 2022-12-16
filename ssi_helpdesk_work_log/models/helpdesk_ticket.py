# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).

from odoo import models


class HelpdeskTicket(models.Model):
    _name = "helpdesk_ticket"
    _inherit = [
        "helpdesk_ticket",
        "mixin.work_object",
    ]

    _work_log_create_page = True
