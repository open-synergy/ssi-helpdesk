# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase, on 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskPriority(HttpSavepointCase):
    """Tour tests for the ``helpdesk_priority`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Grant the configurator group and create the fixtures."""
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        # Pre-Condition: the menu is gated by the configurator group.
        cls.env.ref("ssi_helpdesk.helpdesk_priority_group").sudo().write(
            {"users": [(4, admin.id)]}
        )
        Priority = cls.env["helpdesk_priority"]
        for token, code in (
            ("EDIT", "TOURHDPEDIT"),
            ("DELETE", "TOURHDPDEL"),
            ("DEACTIVATE", "TOURHDPDEACT"),
            ("ACTIVATE", "TOURHDPACT"),
        ):
            record = Priority.create(
                {
                    "name": "TOUR-HDP-%s" % token,
                    "code": code,
                }
            )
            if token == "ACTIVATE":
                # Pre-Condition of the activate tour: starts archived.
                record.write({"active": False})

    def test_create(self):
        """Run the create tour for ``helpdesk_priority``.

        IK: docs/helpdesk_priority/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_priority_create",
            login="admin",
        )

    def test_edit(self):
        """Run the edit tour for ``helpdesk_priority``.

        IK: docs/helpdesk_priority/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_priority_edit",
            login="admin",
        )

    def test_delete(self):
        """Run the delete tour for ``helpdesk_priority``.

        IK: docs/helpdesk_priority/03-delete.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_priority_delete",
            login="admin",
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``helpdesk_priority``.

        IK: docs/helpdesk_priority/04-deactivate.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_priority_deactivate",
            login="admin",
        )

    def test_activate(self):
        """Run the activate tour for ``helpdesk_priority``.

        IK: docs/helpdesk_priority/05-activate.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_priority_activate",
            login="admin",
        )
