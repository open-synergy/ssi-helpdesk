# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase, on 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskTypeCategory(HttpSavepointCase):
    """Tour tests for the ``helpdesk_type_category`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Grant the configurator group and create the fixtures."""
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        # Pre-Condition: the menu is gated by the configurator group.
        cls.env.ref("ssi_helpdesk.helpdesk_type_category_group").sudo().write(
            {"users": [(4, admin.id)]}
        )
        Category = cls.env["helpdesk_type_category"]
        for token, code in (
            ("EDIT", "TOURHDCEDIT"),
            ("DELETE", "TOURHDCDEL"),
            ("DEACTIVATE", "TOURHDCDEACT"),
            ("ACTIVATE", "TOURHDCACT"),
        ):
            record = Category.create({"name": "TOUR-HDC-%s" % token, "code": code})
            if token == "ACTIVATE":
                # Pre-Condition of the activate tour: starts archived.
                record.write({"active": False})

    def test_create(self):
        """Run the create tour for ``helpdesk_type_category``.

        IK: docs/helpdesk_type_category/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_category_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``helpdesk_type_category``.

        IK: docs/helpdesk_type_category/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_category_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``helpdesk_type_category``.

        IK: docs/helpdesk_type_category/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_category_delete",
            login="admin",
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``helpdesk_type_category``.

        IK: docs/helpdesk_type_category/04-deactivate.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_category_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``helpdesk_type_category``.

        IK: docs/helpdesk_type_category/05-activate.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_type_category_activate",
            login="admin",
        )
