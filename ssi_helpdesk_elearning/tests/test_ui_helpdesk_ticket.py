# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: 14.0's HttpCase has no cls.env in
# setUpClass (odoo-development-ui-test, structure-and-runner.md).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskTicketElearning(HttpSavepointCase):
    """Tour test for the e-learning fields on the resolution line."""

    @classmethod
    def setUpClass(cls):
        """Create one draft ticket for the edit tour.

        Adds ``admin`` to the ticket viewer, user, and validator groups
        explicitly so the tour does not depend on the implication chain.
        The ticket date is written explicitly so the fixture does not
        depend on the day the tests run.
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
        company = (
            cls.env["res.partner"]
            .with_user(cls.admin)
            .create({"name": "Tour EL76 Company", "is_company": True})
        )
        contact = (
            cls.env["res.partner"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour EL76 Contact",
                    "parent_id": company.id,
                    "type": "contact",
                }
            )
        )
        cls.ticket = (
            cls.env["helpdesk_ticket"]
            .with_user(cls.admin)
            .create(
                {
                    "title": "Tour EL76 Edit Ticket",
                    "commercial_partner_id": company.id,
                    "partner_id": contact.id,
                    "date": "2026-01-15",
                }
            )
        )

    def test_edit(self):
        """Run the edit tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/02-edit.md (delta -- Additional Fields,
        Modified Flow)
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_elearning_helpdesk_ticket_edit",
            login="admin",
        )
