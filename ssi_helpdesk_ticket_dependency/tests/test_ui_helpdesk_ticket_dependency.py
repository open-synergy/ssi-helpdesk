# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase, on 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskTicketDependency(HttpSavepointCase):
    """Tour tests for the ticket dependency delta work instructions.

    Covers the Dependencies tab on the ticket form. The start and
    confirm gates are invisible validations, covered by the unit tests.
    Tours run as ``admin``.
    """

    @classmethod
    def setUpClass(cls):
        """Grant the access groups and create the ticket for the tour.

        The edit tour opens a plain draft ticket.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        for xml_id in (
            "helpdesk_ticket_viewer_group",
            "helpdesk_ticket_user_group",
            "helpdesk_ticket_validator_group",
        ):
            cls.env.ref("ssi_helpdesk.%s" % xml_id).sudo().write(
                {"users": [(4, cls.admin.id)]}
            )
        cls.company = (
            cls.env["res.partner"]
            .with_user(cls.admin)
            .create({"name": "DEP75 Company", "is_company": True})
        )
        cls.contact = (
            cls.env["res.partner"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "DEP75 Contact",
                    "parent_id": cls.company.id,
                    "type": "contact",
                }
            )
        )
        cls.ticket_edit = cls._create_ticket("DEP75 Edit Ticket")

    @classmethod
    def _create_ticket(cls, title):
        """Create a draft ticket with a fixed date.

        :param title: unique title used as the list-row marker
        :return: the created ``helpdesk_ticket`` record
        """
        return (
            cls.env["helpdesk_ticket"]
            .with_user(cls.admin)
            .create(
                {
                    "title": title,
                    "commercial_partner_id": cls.company.id,
                    "partner_id": cls.contact.id,
                    "date": "2026-01-15",
                }
            )
        )

    def test_helpdesk_ticket_edit(self):
        """Run the Dependencies tab tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_ticket_dependency_helpdesk_ticket_edit",
            login="admin",
        )
