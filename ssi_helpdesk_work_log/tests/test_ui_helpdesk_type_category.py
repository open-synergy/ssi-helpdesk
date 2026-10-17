# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase, on 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskTypeCategoryWorkLog(HttpSavepointCase):
    """Tour tests for the work log delta of ``helpdesk_type_category``."""

    @classmethod
    def setUpClass(cls):
        """Grant the groups that open the menu to ``admin``.

        The tour only opens the create form, so no fixture record is
        needed. ``admin`` is used because the full repository is
        installed in the CI database, including the operating unit glue.
        """
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        for xml_id in ("helpdesk_type_category_group",):
            cls.env.ref("ssi_helpdesk.%s" % xml_id).sudo().write(
                {"users": [(4, admin.id)]}
            )

    def test_create(self):
        """Run the work log delta create tour for ``helpdesk_type_category``.

        IK: docs/helpdesk_type_category/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_work_log_helpdesk_type_category_create",
            login="admin",
        )
