# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class HelpdeskTicketResolutionDocumentation(models.Model):
    _name = "helpdesk_ticket.resolution_documentation"
    _inherit = [
        "helpdesk_ticket.resolution_documentation",
    ]

    course_id = fields.Many2one(
        string="Course",
        comodel_name="slide.channel",
        ondelete="restrict",
    )
    allowed_content_ids = fields.Many2many(
        string="Allowed Content",
        comodel_name="slide.slide",
        compute="_compute_allowed_content_ids",
        store=False,
        compute_sudo=True,
    )
    content_id = fields.Many2one(
        string="Content",
        comodel_name="slide.slide",
        ondelete="restrict",
    )

    @api.onchange(
        "course_id",
    )
    def onchange_content_id(self):
        self.content_id = False

    @api.onchange(
        "content_id",
    )
    def onchange_url(self):
        self.url = False
        if self.content_id:
            self.url = self.content_id.website_url

    @api.onchange(
        "content_id",
    )
    def onchange_name(self):
        self.name = False
        if self.content_id:
            self.name = self.content_id.name

    @api.depends(
        "course_id",
    )
    def _compute_allowed_content_ids(self):
        CourseContent = self.env["slide.slide"]
        for record in self:
            result = False
            if record.course_id:
                criteria = [
                    ("channel_id", "=", record.course_id.id),
                ]
                result = CourseContent.search(criteria)
            record.allowed_content_ids = result
