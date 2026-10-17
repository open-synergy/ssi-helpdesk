# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase, on 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskProject(HttpSavepointCase):
    """Tour tests for the helpdesk and project work instructions.

    Covers the **Project** tab of ``helpdesk_type``, the **Create**
    button of ``helpdesk_ticket`` and the **Open** button of
    ``project.task``. Tours run as ``admin``.
    """

    @classmethod
    def setUpClass(cls):
        """Create the type, project, ticket and task fixtures.

        Adds ``admin`` to the type configurator group and the ticket
        groups, so the tours do not depend on the implication chain.
        ``user_id`` is explicit on the project and the task because
        ``cls.env`` runs as SUPERUSER and the record rules would hide
        them from the tour session.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        cls.env.ref("ssi_helpdesk.helpdesk_type_group").sudo().write(
            {"users": [(4, cls.admin.id)]}
        )
        for xml_id in (
            "helpdesk_ticket_viewer_group",
            "helpdesk_ticket_user_group",
            "helpdesk_ticket_validator_group",
        ):
            cls.env.ref("ssi_helpdesk.%s" % xml_id).sudo().write(
                {"users": [(4, cls.admin.id)]}
            )

        # Category picked by the type create tour.
        cls.category = cls.env["helpdesk_type_category"].create(
            {"name": "PJ80 Category", "code": "PJ80CAT"}
        )

        # Project with one stage, used by the ticket and the task.
        stage = cls.env["project.task.type"].create(
            {"name": "PJ80-STAGE", "sequence": 1, "state": "draft"}
        )
        cls.project = cls.env["project.project"].create(
            {
                "name": "PJ80-PROJECT",
                "user_id": cls.admin.id,
                "type_ids": [(6, 0, [stage.id])],
            }
        )

        # Create task tour -- Pre-Condition: the type has a task template
        # and the ticket has a project.
        cls.type_template = cls.env["helpdesk_type"].create(
            {
                "name": "PJ80-TYPE-TEMPLATE",
                "code": "PJ80TPL",
                "category_id": cls.category.id,
                "need_task": True,
                "task_ids": [(0, 0, {"title": "PJ80-TEMPLATE-TASK"})],
            }
        )
        company = cls.env["res.partner"].create(
            {"name": "PJ80 Company", "is_company": True}
        )
        contact = cls.env["res.partner"].create(
            {"name": "PJ80 Contact", "parent_id": company.id, "type": "contact"}
        )
        cls.ticket_task = cls._create_ticket(
            "PJ80 Task Ticket", company, contact, cls.type_template
        )

        # Open ticket tour -- Pre-Condition: the task is linked to a ticket.
        cls.ticket_linked = cls._create_ticket("PJ80 Linked Ticket", company, contact)
        cls.env["project.task"].create(
            {
                "name": "PJ80-LINKED-TASK",
                "project_id": cls.project.id,
                "user_id": cls.admin.id,
                "ticket_ids": [(6, 0, [cls.ticket_linked.id])],
            }
        )

    @classmethod
    def _create_ticket(cls, title, company, contact, ticket_type=None):
        """Create a draft ``helpdesk_ticket`` bound to the project.

        The date is written explicitly so the fixture does not depend
        on the day the tests run.

        :param title: unique title used as the list-row marker
        :param company: the commercial partner of the ticket
        :param contact: the contact of the ticket
        :param ticket_type: optional ``helpdesk_type`` of the ticket
        :return: the created ``helpdesk_ticket`` record, in Draft
        """
        values = {
            "title": title,
            "commercial_partner_id": company.id,
            "partner_id": contact.id,
            "project_id": cls.project.id,
            "date": "2026-01-15",
        }
        if ticket_type:
            values["type_id"] = ticket_type.id
        return cls.env["helpdesk_ticket"].with_user(cls.admin).create(values)

    def test_type_create(self):
        """Run the type create tour with the Project tab.

        IK: docs/helpdesk_type/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_project_pj80_helpdesk_type_create",
            login="admin",
        )

    def test_ticket_create_task(self):
        """Run the create task tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/09-create-task.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_project_pj80_helpdesk_ticket_create_task",
            login="admin",
        )

    def test_task_open_ticket(self):
        """Run the open ticket tour for ``project.task``.

        IK: docs/project_task/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_project_pj80_project_task_open_ticket",
            login="admin",
        )
