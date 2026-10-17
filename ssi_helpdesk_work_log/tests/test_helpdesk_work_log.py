# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskWorkLog(YamlTransactionCase):
    """Test the work log integration of ``helpdesk_ticket``."""

    def test_helpdesk_work_log(self):
        """Run the ticket scenario with a typed work estimation."""
        self.run_yaml_scenario("test_data_helpdesk_work_log.yaml")
