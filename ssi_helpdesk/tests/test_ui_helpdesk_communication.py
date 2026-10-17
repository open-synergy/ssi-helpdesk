# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskCommunication(HttpSavepointCase):
    """Tour tests for the ``helpdesk_communication`` work instructions.

    Covers create/edit/delete/start/finish/restart/reload followers/
    create ticket (``docs/helpdesk_communication/01-create.md`` through
    ``15-create-ticket.md``). All master data is built from scratch in
    ``setUpClass``. Tours run as ``admin``.
    """

    @classmethod
    def setUpClass(cls):
        """Create shared partners and one fixture record per tour.

        Adds ``admin`` to the communication and ticket groups
        explicitly so the tours do not depend on the implication chain.
        Every tour except create opens a record prepared here in the
        state required by the Pre-Condition of its work instruction.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        for xml_id in (
            "helpdesk_communication_viewer_group",
            "helpdesk_communication_user_group",
            "helpdesk_communication_validator_group",
            "helpdesk_ticket_viewer_group",
            "helpdesk_ticket_user_group",
        ):
            cls.env.ref("ssi_helpdesk.%s" % xml_id).sudo().write(
                {"users": [(4, cls.admin.id)]}
            )

        # Partners picked from dropdowns by the create tour.
        cls.create_company = cls._create_company("Tour HC Create Company")
        cls.create_contact = cls._create_contact(
            "Tour HC Create Contact", cls.create_company
        )

        # Partners shared by every other fixture record.
        cls.company = cls._create_company("Tour HC Shared Company")
        cls.contact = cls._create_contact("Tour HC Shared Contact", cls.company)
        cls.ticket_contact = cls._create_contact("Tour HC Ticket Contact", cls.company)

        # Edit tour -- Pre-Condition: Draft status.
        cls.communication_edit = cls._create_communication("Tour HC Edit Communication")

        # Delete tour -- Pre-Condition: Draft status and document number
        # "/", reached in Python via ``action_reset_document_number()``
        # because a communication is numbered when it is created.
        cls.communication_delete = cls._create_communication(
            "Tour HC Delete Communication"
        )
        # Drop the policy fields cached by create() before the transition.
        cls.communication_delete.invalidate_cache()
        cls.communication_delete.with_user(cls.admin).action_reset_document_number()
        cls.communication_delete.invalidate_cache()

        # Start tour -- Pre-Condition: Draft status.
        cls.communication_start = cls._create_communication(
            "Tour HC Start Communication"
        )

        # Finish tour -- Pre-Condition: On Progress status, reached in
        # Python via ``action_open()``.
        cls.communication_finish = cls._create_communication(
            "Tour HC Finish Communication"
        )
        # Drop the policy fields cached by create() before the transition.
        cls.communication_finish.invalidate_cache()
        cls.communication_finish.with_user(cls.admin).action_open()
        cls.communication_finish.invalidate_cache()

        # Restart tour -- Pre-Condition: On Progress status.
        cls.communication_restart = cls._create_communication(
            "Tour HC Restart Communication"
        )
        # Drop the policy fields cached by create() before the transition.
        cls.communication_restart.invalidate_cache()
        cls.communication_restart.with_user(cls.admin).action_open()
        cls.communication_restart.invalidate_cache()

        # Reload followers tour -- Pre-Condition: # Ticket is filled with a
        # ticket whose contact is not yet a follower.
        cls.ticket = cls._create_ticket("Tour HC Linked Ticket")
        cls.communication_reload = cls._create_communication(
            "Tour HC Reload Communication", ticket=cls.ticket
        )

        # Create ticket tour -- Pre-Condition: # Ticket is empty, and a
        # category with one type exists.
        cls.communication_wizard = cls._create_communication(
            "Tour HC Wizard Communication"
        )
        cls.category = cls.env["helpdesk_type_category"].create(
            {"name": "Tour HC Wizard Category", "code": "TOURHCCAT"}
        )
        cls.ticket_type = cls.env["helpdesk_type"].create(
            {
                "name": "Tour HC Wizard Type",
                "code": "TOURHCTYPE",
                "category_id": cls.category.id,
            }
        )

    @classmethod
    def _create_company(cls, name):
        """Create a company partner (a contact without a parent).

        :param name: unique name typed into the dropdown by the tour
        :return: the created ``res.partner`` record
        """
        return (
            cls.env["res.partner"]
            .with_user(cls.admin)
            .create({"name": name, "is_company": True})
        )

    @classmethod
    def _create_contact(cls, name, company):
        """Create a person contact whose parent is ``company``.

        :param name: unique name typed into the dropdown by the tour
        :param company: the parent ``res.partner`` company
        :return: the created ``res.partner`` record
        """
        return (
            cls.env["res.partner"]
            .with_user(cls.admin)
            .create({"name": name, "parent_id": company.id, "type": "contact"})
        )

    @classmethod
    def _create_communication(cls, title, ticket=None):
        """Create a draft ``helpdesk_communication`` with a fixed date.

        The date is written explicitly so the fixture does not depend
        on the day the tests run.

        :param title: unique title used as the list-row marker
        :param ticket: optional ``helpdesk_ticket`` to link
        :return: the created ``helpdesk_communication`` record, in Draft
        """
        values = {
            "title": title,
            "partner_id": cls.contact.id,
            "date": "2026-01-15",
        }
        if ticket:
            values["ticket_id"] = ticket.id
        return cls.env["helpdesk_communication"].with_user(cls.admin).create(values)

    @classmethod
    def _create_ticket(cls, title):
        """Create a draft ``helpdesk_ticket`` for ``ticket_contact``.

        :param title: title of the ticket
        :return: the created ``helpdesk_ticket`` record, in Draft
        """
        return (
            cls.env["helpdesk_ticket"]
            .with_user(cls.admin)
            .create(
                {
                    "title": title,
                    "commercial_partner_id": cls.company.id,
                    "partner_id": cls.ticket_contact.id,
                    "date": "2026-01-15",
                }
            )
        )

    def test_create(self):
        """Run the create tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/01-create.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_communication_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_communication_edit", login="admin"
        )

    def test_delete(self):
        """Run the delete tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/03-delete.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_communication_delete", login="admin"
        )

    def test_start(self):
        """Run the start tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/07-start.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_communication_start", login="admin"
        )

    def test_finish(self):
        """Run the finish tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/09-finish.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_communication_finish", login="admin"
        )

    def test_restart(self):
        """Run the restart tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/12-restart.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_helpdesk_communication_restart", login="admin"
        )

    def test_reload_followers(self):
        """Run the reload followers tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/14-reload-followers.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_communication_reload_followers",
            login="admin",
        )

    def test_create_ticket(self):
        """Run the create ticket tour for ``helpdesk_communication``.

        IK: docs/helpdesk_communication/15-create-ticket.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_communication_create_ticket",
            login="admin",
        )
