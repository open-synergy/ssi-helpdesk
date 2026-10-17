# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskCommunicationOperatingUnit(HttpSavepointCase):
    """Tour test for the Operating Unit delta of ``helpdesk_communication``.

    Covers ``docs/helpdesk_communication/01-create.md``. The tour runs as
    ``admin``, who must be in the multi operating unit group because
    the field is restricted to that group.
    """

    @classmethod
    def setUpClass(cls):
        """Put ``admin`` in the groups required by the tour.

        Adds ``admin`` to the multi operating unit group and to the
        communication viewer and user groups explicitly, so the tour does not
        depend on the implication chain.
        """
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        cls.env.ref("operating_unit.group_multi_operating_unit").sudo().write(
            {"users": [(4, admin.id)]}
        )
        for xml_id in (
            "helpdesk_communication_viewer_group",
            "helpdesk_communication_user_group",
        ):
            cls.env.ref("ssi_helpdesk.%s" % xml_id).sudo().write(
                {"users": [(4, admin.id)]}
            )

    def test_create(self):
        """Run the create tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_operating_unit_ou81_helpdesk_communication_create",
            login="admin",
        )
