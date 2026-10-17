# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskTicketSplitGate(YamlTransactionCase):
    """Cover the confirm gate on tickets with unfinished split tickets."""

    def test_helpdesk_ticket_split_gate(self):
        """Run the split ticket confirm gate scenarios."""
        self.run_yaml_scenario("test_data_helpdesk_ticket_split_gate.yaml")
