# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskTicketLineOnchange(YamlTransactionCase):
    """Test the onchange of the helpdesk ticket line models."""

    def test_helpdesk_ticket_line_onchange(self):
        """Run the ticket line ``onchange_name`` scenarios.

        The scenarios drive the data requirement and resolution
        documentation line forms with ``action: form`` and check that
        the name follows the selected type.
        """
        self.run_yaml_scenario("test_data_helpdesk_ticket_line_onchange.yaml")
