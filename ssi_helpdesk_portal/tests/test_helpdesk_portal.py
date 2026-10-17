# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskPortal(YamlTransactionCase):
    """Cover the portal extension of the ``helpdesk_ticket`` model."""

    def test_helpdesk_portal(self):
        """Run the ticket scenario with the portal mixin.

        Creates a ticket, reads its website URL and moves it from
        draft to open.
        """
        self.run_yaml_scenario("test_data_helpdesk_portal.yaml")
