# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskWaitingFor(YamlTransactionCase):
    """Cover the Waiting For marker of ``helpdesk_communication``."""

    def test_helpdesk_waiting_for(self):
        """Run the Waiting For and ticket counter scenarios."""
        self.run_yaml_scenario("test_data_helpdesk_waiting_for.yaml")
