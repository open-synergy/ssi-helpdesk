# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskTicketOnchange(YamlTransactionCase):
    """Test the onchange methods of ``helpdesk_ticket``."""

    def test_helpdesk_ticket_onchange(self):
        """Run the helpdesk ticket onchange scenarios.

        The scenarios drive the ticket form with ``action: form`` and
        check contact groups, CC contacts, title, type, duration and
        deadline.
        """
        self.run_yaml_scenario("test_data_helpdesk_ticket_onchange.yaml")
