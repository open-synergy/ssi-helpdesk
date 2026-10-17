# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase, on 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskTicketDependency(HttpSavepointCase):
    """Tour tests for the ticket dependency delta work instructions.

    Covers the Dependencies tab on the ticket form and the start and
    confirm gates. Tours run as ``admin``.
    """

    @classmethod
    def setUpClass(cls):
        """Grant the access groups and create one ticket per tour.

        The edit tour opens a plain draft ticket. The start tour opens a
        ready ticket held by a finish to start dependency, and the
        confirm tour opens an open ticket held by an external
        dependency. Dependencies are added after the transitions so
        that the fixture itself is not blocked.
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
        cls.blocker = cls._create_ticket("DEP75 Blocker Ticket")
        cls.ticket_start = cls._create_ticket("DEP75 Start Ticket")
        cls.ticket_start.with_user(cls.admin).action_ready()
        cls.ticket_start.invalidate_cache()
        cls.env["helpdesk_ticket.dependency"].create(
            {
                "ticket_id": cls.ticket_start.id,
                "blocker_kind": "ticket",
                "blocker_ticket_id": cls.blocker.id,
                "dependency_type": "fs",
            }
        )
        cls.ticket_confirm = cls._create_ticket("DEP75 Confirm Ticket")
        cls.ticket_confirm.with_user(cls.admin).action_ready()
        cls.ticket_confirm.invalidate_cache()
        cls.ticket_confirm.with_user(cls.admin).action_open()
        cls.ticket_confirm.invalidate_cache()
        cls.env["helpdesk_ticket.dependency"].create(
            {
                "ticket_id": cls.ticket_confirm.id,
                "blocker_kind": "external",
                "external_reference": "owner/repo#75",
            }
        )

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

    def test_helpdesk_ticket_start(self):
        """Run the start gate tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/07-start.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_ticket_dependency_helpdesk_ticket_start",
            login="admin",
        )

    def test_helpdesk_ticket_confirm(self):
        """Run the confirm gate tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/04-confirm.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_ticket_dependency_helpdesk_ticket_confirm",
            login="admin",
        )
