# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestHelpdeskAiTrace(YamlTransactionCase):
    """Cover the AI trace mixin on the ``helpdesk_ticket`` model."""

    def test_helpdesk_ai_trace(self):
        """Run the ticket AI trace scenarios of the YAML file."""
        self.run_yaml_scenario("test_data_helpdesk_ai_trace.yaml")

    def test_ticket_form_has_trace_count(self):
        """Expose ``ai_trace_count`` in the ticket form arch.

        Pure Python -- trigger P1 (L-01: the ``fields_view_get`` return
        value is dropped by ``action: call``, so the arch cannot be
        asserted in YAML).
        """
        view = self.env["helpdesk_ticket"].fields_view_get(view_type="form")
        self.assertIn('name="ai_trace_count"', view["arch"])
