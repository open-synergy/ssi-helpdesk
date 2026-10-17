# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskTicketSide(HttpSavepointCase):
    """Tour tests for the side flows of ``helpdesk_ticket``.

    Covers cancel, restart, split and the creation of the finishing
    and updating communications (``docs/helpdesk_ticket/10-cancel.md``,
    ``12-restart.md``, ``15-split.md``,
    ``16-create-finishing-communication.md`` and
    ``17-create-updating-communication.md``). All master data is built
    from scratch in ``setUpClass``. Tours run as ``admin``, which
    belongs to the ticket validator group.
    """

    @classmethod
    def setUpClass(cls):
        """Create shared master data and one fixture ticket per tour.

        Adds ``admin`` to the ticket viewer, user, and validator groups
        explicitly so the tours do not depend on the implication chain.
        Every tour opens a ticket prepared here in the state required
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

        cls.company = cls._create_company("Tour HD Side Company")
        cls.contact = cls._create_contact("Tour HD Side Contact", cls.company)

        # A cancel reason offered to every model; ``global_use`` is what
        # makes it visible in the wizard radio list.
        cls.cancel_reason = cls.env["base.cancel_reason"].create(
            {
                "name": "Tour HD Reason",
                "code": "TOURHD",
                "global_use": True,
            }
        )

        # Split tour -- the category and type picked in the wizard.
        cls.category = cls.env["helpdesk_type_category"].create(
            {"name": "Tour HD Category", "code": "TOURHDCAT"}
        )
        cls.ticket_type = cls.env["helpdesk_type"].create(
            {
                "name": "Tour HD Type",
                "code": "TOURHDTYPE",
                "category_id": cls.category.id,
            }
        )

        # Cancel tour -- Pre-Condition: Draft status.
        cls.ticket_cancel = cls._create_ticket("Tour HD Cancel Ticket")

        # Restart tour -- Pre-Condition: Cancelled status, reached in
        # Python via ``action_cancel()``.
        cls.ticket_restart = cls._create_ticket("Tour HD Restart Ticket")
        cls.ticket_restart.with_user(cls.admin).action_cancel(cls.cancel_reason)
        # _compute_policy fills every policy field at once, so the
        # values cached before the transition must be dropped before the
        # next policy reader.
        cls.ticket_restart.invalidate_cache()

        # Split tour -- Pre-Condition: any existing ticket.
        cls.ticket_split = cls._create_ticket("Tour HD Split Ticket")

        # Finishing communication tour -- Pre-Condition: On Progress
        # status and no finishing communication yet.
        cls.ticket_finishing = cls._create_ticket("Tour HD Finishing Ticket")
        cls.ticket_finishing.with_user(cls.admin).action_ready()
        cls.ticket_finishing.invalidate_cache()
        cls.ticket_finishing.with_user(cls.admin).action_open()
        cls.ticket_finishing.invalidate_cache()

        # Updating communication tour -- Pre-Condition: Draft status.
        cls.ticket_updating = cls._create_ticket("Tour HD Updating Ticket")

    @classmethod
    def _create_company(cls, name):
        """Create a company partner (a contact without a parent).

        :param name: unique name of the company
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

        :param name: unique name of the contact
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

    def test_cancel(self):
        """Run the cancel tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/10-cancel.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_cancel", login="admin")

    def test_restart(self):
        """Run the restart tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/12-restart.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_restart", login="admin")

    def test_split(self):
        """Run the split tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/15-split.md
        """
        self.start_tour("/web", "ssi_helpdesk_helpdesk_ticket_split", login="admin")

    def test_create_finishing_communication(self):
        """Run the finishing communication tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/16-create-finishing-communication.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_ticket_create_finishing_communication",
            login="admin",
        )

    def test_create_updating_communication(self):
        """Run the updating communication tour for ``helpdesk_ticket``.

        IK: docs/helpdesk_ticket/17-create-updating-communication.md
        """
        self.start_tour(
            "/web",
            "ssi_helpdesk_helpdesk_ticket_create_updating_communication",
            login="admin",
        )
