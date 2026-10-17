# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskDataRequirement(YamlTransactionCase):
    """Scenario tests for the helpdesk data requirement glue module.

    Covers a ticket whose type uses the data requirement mixin.
    """

    def test_helpdesk_data_requirement(self):
        """Run the ticket with data requirement scenario.

        Creates a ticket, then moves it from draft to ready and open.
        """
        self.run_yaml_scenario("test_data_helpdesk_data_requirement.yaml")
