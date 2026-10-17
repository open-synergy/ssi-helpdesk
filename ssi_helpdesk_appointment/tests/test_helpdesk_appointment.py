# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskAppointment(YamlTransactionCase):
    """Scenario tests for the appointment fields of ``helpdesk_ticket``."""

    def test_helpdesk_appointment(self):
        """Run the ticket scenario with the appointment integration.

        Covers the default appointment request status of a new ticket
        and the ``draft`` -> ``ready`` -> ``open`` transitions.
        """
        self.run_yaml_scenario("test_data_helpdesk_appointment.yaml")
