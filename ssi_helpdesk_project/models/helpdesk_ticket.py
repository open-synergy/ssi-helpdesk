# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk_ticket"
    _inherit = [
        "helpdesk_ticket",
    ]

    task_ids = fields.Many2many(
        string="Tasks",
        comodel_name="project.task",
        relation="rel_helpdesk_ticket_2_task",
        column1="ticket_id",
        column2="task_id",
    )

    @api.depends(
        "task_ids",
    )
    def _compute_task(self):
        for record in self:
            total_task = len(record.task_ids)
            record.total_task = total_task

    total_task = fields.Integer(
        string="Total Task",
        compute="_compute_task",
        store=True,
    )
