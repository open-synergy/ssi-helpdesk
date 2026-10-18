# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTypeResolutionDocumentation(models.Model):
    """Required resolution documentation template of a helpdesk type.

    Each line names one documentation that every ticket of the type
    must produce. The lines are copied to the ticket when the type is
    selected.
    """

    _name = "helpdesk_type.resolution_documentation"
    _description = "Helpdesk Type Resolution Documentation"
    _order = "type_id, sequence, id"

    type_id = fields.Many2one(
        string="Type",
        comodel_name="helpdesk_type",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=10,
    )
    documentation_type_id = fields.Many2one(
        string="Documentation Type",
        comodel_name="helpdesk_resolution_documentation_type",
        required=True,
        ondelete="restrict",
    )
    name = fields.Char(
        string="Documentation",
        required=True,
    )

    @api.onchange(
        "documentation_type_id",
    )
    def onchange_name(self):
        """Fill the documentation name from the documentation type.

        The name is the documentation type name, or empty when no
        documentation type is selected.
        """
        self.name = False
        if self.documentation_type_id:
            self.name = self.documentation_type_id.name
