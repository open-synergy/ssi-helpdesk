# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSplitHelpdeskTicket(YamlTransactionCase):
    """Cover the access rights and onchange of the split wizard."""

    def test_split_helpdesk_ticket(self):
        """Run the split wizard ACL and onchange scenarios."""
        self.run_yaml_scenario("test_split_helpdesk_ticket.yaml")
