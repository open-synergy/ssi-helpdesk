# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskWorkLogOnchange(YamlTransactionCase):
    """Test the work estimation onchange of ``helpdesk_ticket``."""

    def test_helpdesk_work_log_onchange(self):
        """Run the work estimation onchange scenarios.

        The scenarios drive the ticket form with ``action: form``:
        selecting a type copies its work estimation and clearing the
        type resets the estimation to zero.
        """
        self.run_yaml_scenario("test_data_helpdesk_work_log_onchange.yaml")
