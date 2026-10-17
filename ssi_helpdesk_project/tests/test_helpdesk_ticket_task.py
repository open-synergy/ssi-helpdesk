# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskTicketTask(YamlTransactionCase):
    """Test the task actions of ``helpdesk_ticket``."""

    def setUp(self):
        """Create a ticket linked to one project task.

        The fixture uses unique ``PJ69`` names so that it does not clash
        with records left by the YAML scenarios in the shared
        transaction.
        """
        super().setUp()
        env = self.env
        company = env["res.partner"].create(
            {"name": "PJ69 Company P", "is_company": True}
        )
        contact = env["res.partner"].create(
            {"name": "PJ69 Contact P", "parent_id": company.id}
        )
        project = env["project.project"].create({"name": "PJ69 Project P"})
        self.task = env["project.task"].create(
            {"name": "PJ69 Task P", "project_id": project.id}
        )
        admin = env.ref("base.user_admin")
        self.ticket = (
            env["helpdesk_ticket"]
            .with_user(admin)
            .create(
                {
                    "title": "PJ69 Ticket P",
                    "partner_id": contact.id,
                    "commercial_partner_id": company.id,
                    "project_id": project.id,
                    "task_ids": [(6, 0, [self.task.id])],
                }
            )
        )

    def test_helpdesk_ticket_task(self):
        """Run the task creation and task onchange scenarios.

        The scenarios call ``action_create_task`` and drive the ticket
        form with ``action: form`` for ``onchange_need_task``.
        """
        self.run_yaml_scenario("test_data_helpdesk_ticket_task.yaml")

    def test_action_open_task(self):
        """Check the window action returned by ``action_open_task``.

        Python test because the action returns a dict (P1; L-01, L-02).
        The action must target ``project.task`` and its domain must list
        the tasks of the ticket.
        """
        res = self.ticket.action_open_task()
        self.assertEqual(res["res_model"], "project.task")
        self.assertEqual(res["domain"], [("id", "in", self.ticket.task_ids.ids)])
        self.assertEqual(self.ticket.task_ids, self.task)
