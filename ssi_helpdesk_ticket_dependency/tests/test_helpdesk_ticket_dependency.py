# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskTicketDependency(YamlTransactionCase):
    """Scenario tests for the helpdesk ticket dependency module.

    Covers the start and finish gates for every dependency type, the
    release of a cancelled blocker, the constraints and the blocked
    flags.
    """

    def test_helpdesk_ticket_dependency_gate(self):
        """Run the start and finish gate scenarios."""
        self.run_yaml_scenario("test_data_helpdesk_ticket_dependency_gate.yaml")

    def test_helpdesk_ticket_dependency_rule(self):
        """Run the constraint and blocked flag scenarios."""
        self.run_yaml_scenario("test_data_helpdesk_ticket_dependency_rule.yaml")
