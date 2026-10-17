# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class HelpdeskChannel(models.Model):
    """Master data of channels through which helpdesk tickets are received."""

    _name = "helpdesk_channel"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Helpdesk Channel"
