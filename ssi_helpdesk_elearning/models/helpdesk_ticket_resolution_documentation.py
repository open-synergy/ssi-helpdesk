# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


# Extends the resolution documentation child of a helpdesk ticket with
# an e-learning course and course content, and lets the content fill
# the documentation name and URL.
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
        """Clear the content when the course changes.

        The content must belong to the selected course, so a previously
        chosen content is no longer valid.
        """
        self.content_id = False

    @api.onchange(
        "content_id",
    )
    def onchange_url(self):
        """Fill the URL from the selected content.

        The URL is the website URL of the content, or empty when no
        content is selected.
        """
        self.url = False
        if self.content_id:
            self.url = self.content_id.website_url

    @api.onchange(
        "type_id",
        "content_id",
    )
    def onchange_name(self):
        """Fill the documentation name, keeping the base behavior.

        The base implementation (triggered by ``type_id``) sets the
        name from the documentation type. It runs first so that
        selecting a type keeps working when this module is installed;
        a selected content then takes precedence over the type name.
        """
        super().onchange_name()
        if self.content_id:
            self.name = self.content_id.name

    @api.depends(
        "course_id",
    )
    def _compute_allowed_content_ids(self):
        """Compute the contents that can be chosen for the course.

        The allowed contents are the slides of the selected course, and
        none when no course is selected.
        """
        CourseContent = self.env["slide.slide"]
        for record in self:
            result = False
            if record.course_id:
                criteria = [
                    ("channel_id", "=", record.course_id.id),
                ]
                result = CourseContent.search(criteria)
            record.allowed_content_ids = result
