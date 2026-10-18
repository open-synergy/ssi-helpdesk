# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

EVIDENCE_KIND_SELECTION = [
    ("message", "Message"),
    ("record", "Odoo Record"),
    ("decision", "Decision"),
    ("url", "URL"),
    ("code", "Code"),
]


class HelpdeskResolutionDocumentationType(models.Model):
    """Master data of documentation types used to document ticket resolutions.

    A type defines which evidence a resolution documentation line
    needs before it can be done: the required evidence kind, the
    confirmation of the customer and the root cause.
    """

    _name = "helpdesk_resolution_documentation_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Helpdesk Resolution Documentation Type"

    required_evidence_kind = fields.Selection(
        string="Required Evidence Kind",
        selection=EVIDENCE_KIND_SELECTION,
        required=False,
        help="Kind of evidence that a documentation line of this type "
        "must use. Leave empty to accept any evidence kind.",
    )
    requires_customer_confirmation = fields.Boolean(
        string="Requires Customer Confirmation",
        default=False,
        help="Check this box if the documentation must be proven by a "
        "message sent by the customer, not by the company.",
    )
    third_party = fields.Boolean(
        string="Third Party",
        default=False,
        help="Check this box if a third party is involved in this "
        "kind of documentation. It is informative only.",
    )
    requires_root_cause = fields.Boolean(
        string="Requires Root Cause",
        default=False,
        help="Check this box if a root cause must be filled before a "
        "documentation line of this type is done.",
    )
