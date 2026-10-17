# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase
from psycopg2 import IntegrityError

from odoo.exceptions import ValidationError
from odoo.tests import tagged
from odoo.tools import mute_logger


@tagged("post_install", "-at_install")
class TestHelpdeskPriority(YamlTransactionCase):
    """Cover the ``helpdesk_priority`` master data and ticket priority."""

    def setUp(self):
        """Create the ticket fixtures.

        Fixtures live in ``setUp`` because ``YamlTransactionCase`` does
        not provide ``cls.env`` in ``setUpClass``.
        """
        super().setUp()
        admin = self.env.ref("base.user_admin")
        company = self.env["res.partner"].create(
            {"name": "HPT Company", "is_company": True}
        )
        self.contact = self.env["res.partner"].create(
            {
                "name": "HPT Contact",
                "is_company": False,
                "parent_id": company.id,
            }
        )
        self.company = company
        self.ticket_model = self.env["helpdesk_ticket"].with_user(admin)
        self.urgent = self.env.ref("ssi_helpdesk.helpdesk_priority_urgent")
        self.low = self.env.ref("ssi_helpdesk.helpdesk_priority_low")

    def _create_ticket(self, title, priority):
        """Create a draft ticket with the given priority.

        :param title: ticket title
        :param priority: ``helpdesk_priority`` record
        :return: the created ``helpdesk_ticket`` record
        """
        return self.ticket_model.create(
            {
                "title": title,
                "partner_id": self.contact.id,
                "commercial_partner_id": self.company.id,
                "priority_id": priority.id,
            }
        )

    def test_helpdesk_priority(self):
        """Run the priority master data and default scenarios."""
        self.run_yaml_scenario("test_data_helpdesk_priority.yaml")

    def test_priority_required(self):
        """Emptying the priority of a ticket is rejected.

        Pure Python - trigger P5 (L-22: ``psycopg2.IntegrityError`` is
        outside the 12 ``expect_error`` types).
        """
        ticket = self._create_ticket("HPT Required", self.low)
        with mute_logger("odoo.sql_db"), self.assertRaises(
            (IntegrityError, ValidationError)
        ), self.cr.savepoint():
            ticket.write({"priority_id": False})
            ticket.flush()

    def test_ticket_order(self):
        """Tickets are listed by priority sequence, urgent first.

        Pure Python - trigger P1 (L-01: the ``search()`` return value
        and its order cannot be asserted from YAML).
        """
        low = self._create_ticket("HPT Order Low", self.low)
        urgent = self._create_ticket("HPT Order Urgent", self.urgent)
        found = self.ticket_model.search([("id", "in", [low.id, urgent.id])])
        self.assertEqual(found.ids, [urgent.id, low.id])
