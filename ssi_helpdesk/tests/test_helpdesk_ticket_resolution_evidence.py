# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskTicketResolutionEvidence(YamlTransactionCase):
    """Test the evidence of the helpdesk ticket resolution documentation."""

    def test_helpdesk_ticket_resolution_evidence(self):
        """Run the resolution documentation evidence scenario.

        The scenario checks the state per evidence kind, the author and
        channel read from the evidence message, the compatibility of
        lines without kind, and the note logged on the ticket.
        """
        self.run_yaml_scenario("test_data_helpdesk_ticket_resolution_evidence.yaml")
