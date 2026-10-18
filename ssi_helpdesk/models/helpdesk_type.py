# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HelpdeskType(models.Model):
    """Master data of helpdesk ticket types, grouped by category."""

    _name = "helpdesk_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Helpdesk Type"

    category_id = fields.Many2one(
        string="Category",
        comodel_name="helpdesk_type_category",
        required=True,
    )
    duration_id = fields.Many2one(
        string="Duration",
        comodel_name="base.duration",
    )
    priority_id = fields.Many2one(
        string="Default Priority",
        comodel_name="helpdesk_priority",
        ondelete="restrict",
        help="""Default priority of tickets with this type

* Leave empty if this type does not set a default priority
* Selecting this type on a ticket fills the ticket priority""",
    )
    resolution_documentation_template_ids = fields.One2many(
        string="Required Resolution Documentations",
        comodel_name="helpdesk_type.resolution_documentation",
        inverse_name="type_id",
        help="""Required resolution documentations of this type

* Only required documentations are listed here
* Selecting this type on a ticket adds them to the ticket
* Optional documentations are written manually on the ticket""",
    )
