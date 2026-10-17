# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase, on 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskType(HttpSavepointCase):
    """Tour tests for the ``helpdesk_type`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Grant the configurator group and create the fixtures."""
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        # Pre-Condition: the menu is gated by the configurator group.
        cls.env.ref("ssi_helpdesk.helpdesk_type_group").sudo().write(
            {"users": [(4, admin.id)]}
        )
        # Category picked by the create tour and used by the fixtures.
        category = cls.env["helpdesk_type_category"].create(
            {"name": "TOUR HDT Category", "code": "TOURHDTCAT"}
        )
        Type = cls.env["helpdesk_type"]
        for token, code in (
            ("EDIT", "TOURHDTEDIT"),
            ("DELETE", "TOURHDTDEL"),
            ("DEACTIVATE", "TOURHDTDEACT"),
            ("ACTIVATE", "TOURHDTACT"),
        ):
            record = Type.create(
                {
                    "name": "TOUR-HDT-%s" % token,
                    "code": code,
                    "category_id": category.id,
                }
            )
            if token == "ACTIVATE":
                # Pre-Condition of the activate tour: starts archived.
                record.write({"active": False})

    def test_create(self):
        """Run the create tour for ``helpdesk_type``.

        IK: docs/helpdesk_type/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``helpdesk_type``.

        IK: docs/helpdesk_type/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``helpdesk_type``.

        IK: docs/helpdesk_type/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_delete",
            login="admin",
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``helpdesk_type``.

        IK: docs/helpdesk_type/04-deactivate.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``helpdesk_type``.

        IK: docs/helpdesk_type/05-activate.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_activate",
            login="admin",
        )
