# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskTicketResolutionCancel(YamlTransactionCase):
    """Test the not applicable lines of the resolution documentation."""

    def test_helpdesk_ticket_resolution_cancel(self):
        """Run the not applicable resolution documentation scenario.

        The scenario checks the mandatory reason, the cancel state of
        the line and that the ticket documentation status ignores the
        not applicable lines.
        """
        self.run_yaml_scenario("test_data_helpdesk_ticket_resolution_cancel.yaml")
