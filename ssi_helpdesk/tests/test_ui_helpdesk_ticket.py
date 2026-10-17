# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskTicket(HttpSavepointCase):
    """Tour tests for the ``helpdesk_ticket`` work instructions.

    Covers create/edit/delete/confirm/approve/reject/start/ready
    (``docs/helpdesk_ticket/01-create.md`` through ``08-ready.md``).
    All master data is built from scratch in ``setUpClass``. Tours run
    as ``admin``, which belongs to the ticket validator group.
    """

    @classmethod
    def setUpClass(cls):
        """Create shared partners and one fixture ticket per tour.

        Adds ``admin`` to the ticket viewer, user, and validator groups
        explicitly so the tours do not depend on the implication chain.
        The create tour only needs its own company and contact; every
        other tour opens a ticket prepared here in the state required
        by the Pre-Condition of its work instruction.
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

        # Partners picked from dropdowns by the create tour.
        cls.create_company = cls._create_company("Tour HD Create Company")
        cls.create_contact = cls._create_contact(
            "Tour HD Create Contact", cls.create_company
        )

        # Partners shared by every other fixture ticket.
        cls.company = cls._create_company("Tour HD Shared Company")
        cls.contact = cls._create_contact("Tour HD Shared Contact", cls.company)

        # Edit tour -- Pre-Condition: Draft status.
        cls.ticket_edit = cls._create_ticket("Tour HD Edit Ticket")

        # Delete tour -- Pre-Condition: Draft status, number is "/". A
        # ticket is numbered when it is created, so the number is reset
        # through the Reset Document Number action (manual_number_ok).
        cls.ticket_delete = cls._create_ticket("Tour HD Delete Ticket")
        cls.ticket_delete.with_user(cls.admin).action_reset_document_number()
        cls.ticket_delete.invalidate_cache()

        # Ready tour -- Pre-Condition: Draft status.
        cls.ticket_ready = cls._create_ticket("Tour HD Ready Ticket")

        # Start tour -- Pre-Condition: Ready to Start status, reached in
        # Python via ``action_ready()``.
        cls.ticket_start = cls._create_ticket("Tour HD Start Ticket")
        cls.ticket_start.with_user(cls.admin).action_ready()
        # _compute_policy fills every policy field at once and is not
        # context dependent, so the value cached before the transition
        # must be dropped before the next policy reader.
        cls.ticket_start.invalidate_cache()

        # Confirm tour -- Pre-Condition: On Progress status.
        cls.ticket_confirm = cls._create_ticket("Tour HD Confirm Ticket")
        cls.ticket_confirm.with_user(cls.admin).action_ready()
        cls.ticket_confirm.invalidate_cache()
        cls.ticket_confirm.with_user(cls.admin).action_open()
        cls.ticket_confirm.invalidate_cache()

        # Approve tour -- Pre-Condition: Waiting for Approval status.
        cls.ticket_approve = cls._create_ticket("Tour HD Approve Ticket")
        cls._move_to_confirm(cls.ticket_approve)

        # Reject tour -- Pre-Condition: Waiting for Approval status.
        cls.ticket_reject = cls._create_ticket("Tour HD Reject Ticket")
        cls._move_to_confirm(cls.ticket_reject)

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
    def _create_ticket(cls, title):
        """Create a draft ``helpdesk_ticket`` with a fixed date.

        The date is written explicitly so the fixture does not depend
        on the day the tests run.

        :param title: unique title used as the list-row marker
        :return: the created ``helpdesk_ticket`` record, in Draft
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

    @classmethod
    def _move_to_confirm(cls, ticket):
        """Move ``ticket`` from Draft to Waiting for Approval.

        Uses the action methods, not ``write()``, so that sequence
        numbering and approval creation run as in the UI. The cache is
        invalidated after every transition because the policy fields
        are computed together and cached across users.

        :param ticket: a draft ``helpdesk_ticket`` record
        """
        ticket.with_user(cls.admin).action_ready()
        ticket.invalidate_cache()
        ticket.with_user(cls.admin).action_open()
        ticket.invalidate_cache()
        ticket.with_user(cls.admin).action_confirm()
        # approve_ok and reject_ok read active_approver_user_ids, which
        # is computed from the approval records action_confirm() just
        # created; the stale cached value must be dropped first.
        ticket.invalidate_cache()

    def test_create(self):
        """Run the create tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/01-create.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_create", login="admin")

    def test_edit(self):
        """Run the edit tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/02-edit.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_edit", login="admin")

    def test_delete(self):
        """Run the delete tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/03-delete.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_delete", login="admin")

    def test_confirm(self):
        """Run the confirm tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/04-confirm.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_confirm", login="admin")

    def test_approve(self):
        """Run the approve tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/05-approve.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_approve", login="admin")

    def test_reject(self):
        """Run the reject tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/06-reject.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_reject", login="admin")

    def test_start(self):
        """Run the start tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/07-start.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_start", login="admin")

    def test_ready(self):
        """Run the ready tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/08-ready.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_ready", login="admin")
