# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: 14.0's HttpCase has no ``cls.env`` in
# ``setUpClass``.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskChannel(HttpSavepointCase):
    """Tour tests for the ``helpdesk_channel`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the ``helpdesk_channel`` records the tours edit, delete and toggle.

        The ``helpdesk_channel_group`` group already includes the ``admin``
        user by default (see ``security/res_group_data.xml``), so no extra
        group setup is required for the tours.
        """
        super().setUpClass()
        Model = cls.env["helpdesk_channel"]
        vals = {"code": "/"}
        cls.record_edit = Model.create(dict(vals, name="TOUR Channel Edit"))
        cls.record_delete = Model.create(dict(vals, name="TOUR Channel Delete"))
        cls.record_deactivate = Model.create(dict(vals, name="TOUR Channel Deactivate"))
        cls.record_activate = Model.create(
            dict(vals, name="TOUR Channel Activate", active=False)
        )

    def test_create(self):
        """Run the create tour for ``helpdesk_channel``.

        IK: docs/helpdesk_channel/01-create.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_channel_create", login="admin")

    def test_edit(self):
        """Run the edit tour for ``helpdesk_channel``.

        IK: docs/helpdesk_channel/02-edit.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_channel_edit", login="admin")

    def test_delete(self):
        """Run the delete tour for ``helpdesk_channel``.

        IK: docs/helpdesk_channel/03-delete.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_channel_delete", login="admin")

    def test_deactivate(self):
        """Run the deactivate tour for ``helpdesk_channel``.

        IK: docs/helpdesk_channel/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_channel_deactivate", login="admin"
        )

    def test_activate(self):
        """Run the activate tour for ``helpdesk_channel``.

        IK: docs/helpdesk_channel/05-activate.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_channel_activate", login="admin")
