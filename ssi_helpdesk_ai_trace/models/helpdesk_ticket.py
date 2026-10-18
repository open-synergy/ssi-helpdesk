# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class HelpdeskTicket(models.Model):
    _name = "helpdesk_ticket"
    _inherit = [
        "helpdesk_ticket",
        "mixin.ai_trace",
    ]

    # Delta: the ticket gains the AI trace timeline (ai_trace_ids,
    # ai_trace_count) and its Chatter | AI Trace toggle. The mixin adds the
    # toggle marker to the form through fields_view_get, so no view is edited.
