# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSSIHelpdeskOperatingUnit(YamlTransactionCase):
    """Run the Operating Unit scenarios of the helpdesk glue module.

    The scenario file covers the record rules that restrict
    ``helpdesk_ticket`` and ``helpdesk_communication`` per operating
    unit.
    """

    def test_ssi_helpdesk_operating_unit(self):
        """Run the Operating Unit YAML scenario file.

        Executes ``test_data_ssi_helpdesk_operating_unit.yaml`` in one
        transaction.
        """
        self.run_yaml_scenario("test_data_ssi_helpdesk_operating_unit.yaml")
