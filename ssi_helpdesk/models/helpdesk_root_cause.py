# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class HelpdeskRootCause(models.Model):
    """Master data of root causes of helpdesk tickets.

    A root cause is chosen on a resolution documentation line whose
    type requires it.
    """

    _name = "helpdesk_root_cause"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Helpdesk Root Cause"
