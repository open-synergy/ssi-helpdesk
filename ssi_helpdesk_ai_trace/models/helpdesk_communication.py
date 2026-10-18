# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class HelpdeskCommunication(models.Model):
    _name = "helpdesk_communication"
    _inherit = [
        "helpdesk_communication",
        "mixin.ai_trace",
    ]

    # Delta: each communication thread gains its own AI trace timeline
    # (ai_trace_ids, ai_trace_count) and the Chatter | AI Trace toggle. The
    # mixin adds the toggle marker to the form through fields_view_get, so
    # no view is edited.
