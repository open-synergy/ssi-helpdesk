# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskOdooImplementation(YamlTransactionCase):
    """Scenario tests for the Odoo implementation ticket extension."""

    def test_helpdesk_odoo_implementation(self):
        """Run the ticket integration scenario.

        Creates a ticket and moves it through ``ready`` and ``open``.
        """
        self.run_yaml_scenario("test_data_helpdesk_odoo_implementation.yaml")
