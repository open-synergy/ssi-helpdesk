# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk_ticket"
    _inherit = [
        "helpdesk_ticket",
    ]

    need_task = fields.Boolean(
        string="Need Task",
        default=False,
    )
    task_ids = fields.Many2many(
        string="Tasks",
        comodel_name="project.task",
        relation="rel_helpdesk_ticket_2_task",
        column1="ticket_id",
        column2="task_id",
    )
    total_task = fields.Integer(
        string="Total Task",
        compute="_compute_task",
        store=True,
    )
    timebox_latest_id = fields.Many2one(
        string="Letest Timebox",
        comodel_name="task.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_latest_date_start = fields.Date(
        string="Latest Timebox Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_latest_date_end = fields.Date(
        string="Lates Timebox Date End",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_id = fields.Many2one(
        string="Timebox Initial",
        comodel_name="task.timebox",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_date_start = fields.Date(
        string="Timebox Initial Date Start",
        compute="_compute_timebox",
        store=True,
    )
    timebox_initial_date_end = fields.Date(
        string="Timebox Initial Date End",
        compute="_compute_timebox",
        store=True,
    )

    @api.depends(
        "task_ids",
    )
    def _compute_task(self):
        for record in self:
            total_task = len(record.task_ids)
            record.total_task = total_task

    @api.depends(
        "task_ids",
        "task_ids.timebox_latest_id",
        "task_ids.timebox_date_start",
        "task_ids.timebox_date_end",
        "task_ids.timebox_initial_id",
        "task_ids.timebox_initial_date_start",
        "task_ids.timebox_initial_date_end",
        "task_ids.timebox_upcoming_id",
        "task_ids.timebox_upcoming_date_start",
        "task_ids.timebox_upcoming_date_end",
    )
    def _compute_timebox(self):
        for document in self:
            timebox_latest_id = (
                timebox_latest_date_start
            ) = (
                timebox_latest_date_end
            ) = (
                timebox_initial_id
            ) = timebox_initial_date_start = timebox_initial_date_end = False

            if document.task_ids:
                tasks = document.task_ids
                latest_sorted = tasks.sorted(key=lambda r: r.timebox_latest_id)
                timebox_latest_id = latest_sorted[0].timebox_latest_id
                timebox_latest_date_start = timebox_latest_id.date_start
                timebox_latest_date_end = timebox_latest_id.date_end
                initial_sorted = tasks.sorted(key=lambda r: r.timebox_initial_id)
                timebox_initial_id = initial_sorted[-1].timebox_initial_id
                timebox_initial_date_start = timebox_initial_id.date_start
                timebox_initial_date_end = timebox_initial_id.date_end

            document.timebox_latest_id = timebox_latest_id
            document.timebox_latest_date_start = timebox_latest_date_start
            document.timebox_latest_date_end = timebox_latest_date_end
            document.timebox_initial_id = timebox_initial_id
            document.timebox_initial_date_start = timebox_initial_date_start
            document.timebox_initial_date_end = timebox_initial_date_end
