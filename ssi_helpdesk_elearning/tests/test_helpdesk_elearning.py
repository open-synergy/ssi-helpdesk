# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskElearning(YamlTransactionCase):
    """Scenario tests for the e-learning resolution documentation."""

    def test_helpdesk_elearning(self):
        """Run the resolution documentation state scenario.

        Covers the state of a documentation line with and without a
        URL and the resulting ticket documentation state.
        """
        self.run_yaml_scenario("test_data_helpdesk_elearning.yaml")

    def test_helpdesk_elearning_onchange(self):
        """Run the onchange scenarios of the documentation line.

        Covers ``onchange_name``, ``onchange_url`` and
        ``onchange_content_id`` through the form, including the base
        ``type_id`` trigger that this module must keep working.
        """
        self.run_yaml_scenario("test_data_helpdesk_elearning_onchange.yaml")
