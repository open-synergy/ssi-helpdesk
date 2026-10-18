# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HelpdeskPriority(models.Model):
    """Master data of helpdesk ticket priorities.

    Priorities are ordered by ``sequence``: the smaller the sequence,
    the higher the priority. Tickets are listed following this order.
    """

    _name = "helpdesk_priority"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Helpdesk Priority"
    _order = "sequence, id"

    sequence = fields.Integer(
        string="Sequence",
        default=10,
        required=True,
        help="""Priority order

* Lower sequence means higher priority
* Tickets are listed following this order""",
    )
