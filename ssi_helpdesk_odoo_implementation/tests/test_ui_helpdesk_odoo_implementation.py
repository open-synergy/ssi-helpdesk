# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskOdooImplementation(HttpSavepointCase):
    """Tour tests for the Odoo implementation ticket extension.

    Covers the delta work instruction
    ``docs/helpdesk_ticket/01-create.md``. The tour runs as ``admin``.
    """

    @classmethod
    def setUpClass(cls):
        """Give ``admin`` the ticket viewer and user groups.

        The groups are added explicitly so the tour does not depend on
        the implication chain. No master data is needed because the
        tour does not save the form.
        """
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        for xml_id in (
            "helpdesk_ticket_viewer_group",
            "helpdesk_ticket_user_group",
        ):
            cls.env.ref("ssi_helpdesk.%s" % xml_id).sudo().write(
                {"users": [(4, admin.id)]}
            )

    def test_create(self):
        """Run the create tour for the Odoo implementation fields.

        IK: docs/helpdesk_ticket/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_odoo_implementation_helpdesk_ticket_create",
            login="admin",
        )
