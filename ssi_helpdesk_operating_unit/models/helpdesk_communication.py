# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class HelpdeskCommunication(models.Model):  # pylint: disable=too-few-public-methods
    _name = "helpdesk_communication"
    _inherit = [
        "helpdesk_communication",
        "mixin.single_operating_unit",
    ]
