# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskTypeResolutionDocumentation(YamlTransactionCase):
    """Test the resolution documentation template of ``helpdesk_type``."""

    def test_helpdesk_type_resolution_documentation(self):
        """Run the resolution documentation template scenarios.

        The scenarios check that selecting a type fills the ticket
        lines without duplicates, and the template line CRUD.
        """
        self.run_yaml_scenario("test_data_helpdesk_type_resolution_documentation.yaml")
