# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: 14.0's HttpCase has no ``cls.env`` in
# ``setUpClass``.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskContactGroup(HttpSavepointCase):
    """Tour tests for the ``helpdesk_contact_group`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the records that the tours edit, delete and toggle.

        The ``helpdesk_contact_group_configurator_group`` group already
        includes the ``admin`` user by default (see
        ``security/res_group_data.xml``), so no extra group setup is
        required for the tours.
        """
        super().setUpClass()
        cls.company = cls.env["res.partner"].create(
            {"name": "TOUR HDG Company", "is_company": True}
        )
        cls.contact = cls.env["res.partner"].create({"name": "TOUR HDG Contact"})
        Model = cls.env["helpdesk_contact_group"]
        vals = {
            "code": "/",
            "commercial_contact_id": cls.company.id,
            "contact_ids": [(6, 0, cls.contact.ids)],
        }
        cls.record_edit = Model.create(dict(vals, name="TOUR Contact Group Edit"))
        cls.record_delete = Model.create(dict(vals, name="TOUR Contact Group Delete"))
        cls.record_deactivate = Model.create(
            dict(vals, name="TOUR Contact Group Deactivate")
        )
        cls.record_activate = Model.create(
            dict(vals, name="TOUR Contact Group Activate", active=False)
        )

    def test_create(self):
        """Run the create tour for ``helpdesk_contact_group``.

        IK: docs/helpdesk_contact_group/01-create.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_contact_group_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``helpdesk_contact_group``.

        IK: docs/helpdesk_contact_group/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_contact_group_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``helpdesk_contact_group``.

        IK: docs/helpdesk_contact_group/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_contact_group_delete", login="admin"
        )

    def test_deactivate(self):
        """Run the deactivate tour for ``helpdesk_contact_group``.

        IK: docs/helpdesk_contact_group/04-deactivate.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_contact_group_deactivate", login="admin"
        )

    def test_activate(self):
        """Run the activate tour for ``helpdesk_contact_group``.

        IK: docs/helpdesk_contact_group/05-activate.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_contact_group_activate", login="admin"
        )
