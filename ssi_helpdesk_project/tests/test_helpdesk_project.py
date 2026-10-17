# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskProject(YamlTransactionCase):
    """Scenario tests for the helpdesk and project integration.

    Covers a ticket carrying the project fields of
    ``ssi_helpdesk_project`` through its draft, ready and open states.
    """

    def test_helpdesk_project(self):
        """Run the ticket with project integration scenario."""
        self.run_yaml_scenario("test_data_helpdesk_project.yaml")
