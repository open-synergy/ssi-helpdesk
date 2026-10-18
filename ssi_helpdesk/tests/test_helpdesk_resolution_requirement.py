# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskResolutionRequirement(YamlTransactionCase):
    """Test the requirements of resolution documentation types."""

    def test_helpdesk_resolution_requirement(self):
        """Run the resolution documentation requirement scenario.

        The scenario checks the root cause master data, the required
        evidence kind, the customer confirmation, the root cause
        requirement, and the lines of a type without requirement.
        """
        self.run_yaml_scenario("test_data_helpdesk_resolution_requirement.yaml")
