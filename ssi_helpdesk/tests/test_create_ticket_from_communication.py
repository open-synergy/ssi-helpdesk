# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestCreateTicketFromCommunication(YamlTransactionCase):
    """Test the create ticket from communication wizard."""

    def test_create_ticket_from_communication(self):
        """Run the wizard ACL and onchange scenarios."""
        self.run_yaml_scenario("test_data_create_ticket_from_communication.yaml")
