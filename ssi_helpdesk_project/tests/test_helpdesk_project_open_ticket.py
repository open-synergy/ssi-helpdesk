# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskProjectOpenTicket(YamlTransactionCase):
    """Cover ``project.task.action_open_ticket``."""

    def setUp(self):
        """Create a partner, a ticket and a task linked to the ticket."""
        super().setUp()
        env = self.env
        company = env["res.partner"].create(
            {"name": "PJ70 Company", "is_company": True}
        )
        contact = env["res.partner"].create(
            {"name": "PJ70 Contact", "parent_id": company.id}
        )
        self.ticket = env["helpdesk_ticket"].create(
            {
                "title": "PJ70 Ticket",
                "partner_id": contact.id,
                "commercial_partner_id": company.id,
                "need_task": False,
            }
        )
        self.task_with = env["project.task"].create(
            {"name": "PJ70 Task", "ticket_ids": [(6, 0, self.ticket.ids)]}
        )
        self.task_without = env["project.task"].create({"name": "PJ70 Lone"})

    def test_open_ticket_linked(self):
        """Return an action pointing to the linked ticket.

        Pure Python because the method returns a dict (P1, L-01, L-02).
        """
        res = self.task_with.action_open_ticket()
        self.assertEqual(res["res_model"], "helpdesk_ticket")
        self.assertEqual(res["domain"], [("id", "in", self.ticket.ids)])

    def test_open_ticket_without_ticket(self):
        """Return an action with an empty domain when no ticket is linked.

        Pure Python because the method returns a dict (P1, L-01, L-02).
        """
        res = self.task_without.action_open_ticket()
        self.assertEqual(res["res_model"], "helpdesk_ticket")
        self.assertEqual(res["domain"], [("id", "in", [])])
