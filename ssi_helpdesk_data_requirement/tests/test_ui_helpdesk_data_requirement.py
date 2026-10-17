# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase, on 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskDataRequirement(HttpSavepointCase):
    """Tour tests for the data requirement delta work instructions.

    Covers the Data Requirements tab on the helpdesk type form and on
    the helpdesk ticket form. Tours run as ``admin``.
    """

    @classmethod
    def setUpClass(cls):
        """Grant the access groups and create one type and one ticket.

        The type and the ticket carry the ``DR75`` marker so the tours
        open exactly these records from the lists.
        """
        super().setUpClass()
        admin = cls.env.ref("base.user_admin")
        for xml_id in (
            "helpdesk_type_group",
            "helpdesk_ticket_viewer_group",
            "helpdesk_ticket_user_group",
            "helpdesk_ticket_validator_group",
        ):
            cls.env.ref("ssi_helpdesk.%s" % xml_id).sudo().write(
                {"users": [(4, admin.id)]}
            )
        category = cls.env["helpdesk_type_category"].create(
            {"name": "DR75 Category", "code": "DR75CAT"}
        )
        cls.ticket_type = cls.env["helpdesk_type"].create(
            {"name": "DR75-TYPE", "code": "DR75TYPE", "category_id": category.id}
        )
        company = (
            cls.env["res.partner"]
            .with_user(admin)
            .create({"name": "DR75 Company", "is_company": True})
        )
        contact = (
            cls.env["res.partner"]
            .with_user(admin)
            .create(
                {"name": "DR75 Contact", "parent_id": company.id, "type": "contact"}
            )
        )
        cls.ticket = (
            cls.env["helpdesk_ticket"]
            .with_user(admin)
            .create(
                {
                    "title": "DR75 Ticket",
                    "commercial_partner_id": company.id,
                    "partner_id": contact.id,
                    "type_id": cls.ticket_type.id,
                    "date": "2026-01-15",
                }
            )
        )

    def test_helpdesk_type_edit(self):
        """Run the Data Requirements tab tour for ``helpdesk_type``.

        IK: docs/helpdesk_type/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_data_requirement_helpdesk_type_edit",
            login="admin",
        )

    def test_helpdesk_ticket_edit(self):
        """Run the Data Requirements tab tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_data_requirement_helpdesk_ticket_edit",
            login="admin",
        )
