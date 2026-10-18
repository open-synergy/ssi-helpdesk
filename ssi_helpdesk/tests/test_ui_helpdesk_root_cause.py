# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskRootCause(HttpSavepointCase):
    """Tour tests for the root cause work instructions."""

    @classmethod
    def setUpClass(cls):
        """Prepare the group, sequence template, and fixture records.

        Grants the admin user the configurator group the menu is gated
        by, creates the ``sequence.template`` the Generate Code inline
        action needs to succeed, and one fixture record per
        edit/delete/deactivate/activate tour.
        """
        super().setUpClass()
        # Pre-Condition: the menu is gated by the configurator group.
        # Without it the tour dies on its first step because the menu
        # is never rendered.
        cls.env.ref("ssi_helpdesk.helpdesk_root_cause_group").sudo().write(
            {"users": [(4, cls.env.ref("base.user_admin").id)]}
        )

        # Config: a sequence.template for this model is what makes the
        # Generate Code inline action (docs/helpdesk_root_cause/
        # 01-create.md, step 5) succeed instead of raising UserError.
        cls.sequence = cls.env["ir.sequence"].create(
            {
                "name": "Tour Helpdesk Root Cause Sequence",
                "code": "tour.helpdesk.root.cause",
                "prefix": "TOUR-HDR-ROOT-SEQ",
                "padding": 4,
            }
        )
        sequence_field = cls.env["ir.model.fields"].search(
            [
                ("model", "=", "helpdesk_root_cause"),
                ("name", "=", "code"),
            ],
            limit=1,
        )
        date_field = cls.env["ir.model.fields"].search(
            [
                ("model", "=", "helpdesk_root_cause"),
                ("name", "=", "write_date"),
            ],
            limit=1,
        )
        cls.env["sequence.template"].create(
            {
                "name": "Tour Helpdesk Root Cause Sequence Template",
                "model_id": cls.env["ir.model"]._get("helpdesk_root_cause").id,
                "sequence_field_id": sequence_field.id,
                "date_field_id": date_field.id,
                "computation_method": "use_domain",
                "domain": "[]",
                "sequence_selection_method": "use_sequence",
                "sequence_id": cls.sequence.id,
            }
        )

        # Fixture for the edit tour -- a record whose Name the tour
        # changes to a distinct value.
        cls.type_edit = cls.env["helpdesk_root_cause"].create(
            {
                "name": "Tour HDR Root Edit",
                "code": "TOUR-HDR-ROOT-EDIT",
            }
        )

        # Fixture for the delete tour -- Pre-Condition: not referenced
        # by any ticket line, so it always qualifies.
        cls.type_delete = cls.env["helpdesk_root_cause"].create(
            {
                "name": "Tour HDR Root Delete",
                "code": "TOUR-HDR-ROOT-DEL",
            }
        )

        # Fixture for the deactivate tour -- Pre-Condition: active
        # (``mixin.master_data`` default).
        cls.type_deactivate = cls.env["helpdesk_root_cause"].create(
            {
                "name": "Tour HDR Root Deactivate",
                "code": "TOUR-HDR-ROOT-DEACT",
            }
        )

        # Fixture for the activate tour -- Pre-Condition: archived,
        # reached in Python rather than through the deactivate tour.
        cls.type_activate = cls.env["helpdesk_root_cause"].create(
            {
                "name": "Tour HDR Root Activate",
                "code": "TOUR-HDR-ROOT-ACT",
            }
        )
        cls.type_activate.write({"active": False})

    def test_create(self):
        """Run the create tour for ``helpdesk_root_cause``.

        IK: docs/helpdesk_root_cause/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_root_cause_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``helpdesk_root_cause``.

        IK: docs/helpdesk_root_cause/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_root_cause_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``helpdesk_root_cause``.

        IK: docs/helpdesk_root_cause/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_root_cause_delete",
            login="admin",
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``helpdesk_root_cause``.

        IK: docs/helpdesk_root_cause/04-deactivate.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_root_cause_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``helpdesk_root_cause``.

        IK: docs/helpdesk_root_cause/05-activate.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_root_cause_activate",
            login="admin",
        )
