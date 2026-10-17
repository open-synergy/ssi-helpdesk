# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHelpdeskAppointment(HttpSavepointCase):
    """Tour tests for the appointment extension of ``helpdesk_ticket``.

    Covers the delta work instruction
    ``docs/helpdesk_ticket/02-edit.md``. All master data is built from
    scratch in ``setUpClass``. Tours run as ``admin``.
    """

    @classmethod
    def setUpClass(cls):
        """Create one draft ticket and one draft appointment request.

        Adds ``admin`` to the ticket and appointment request groups
        explicitly so the tour does not depend on the implication
        chain. The appointment request is created in Draft by ``admin``
        and is not yet linked to any ticket, as the Pre-Condition of the
        work instruction requires.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        for xml_id in (
            "ssi_helpdesk.helpdesk_ticket_viewer_group",
            "ssi_helpdesk.helpdesk_ticket_user_group",
            "ssi_helpdesk.helpdesk_ticket_validator_group",
            "ssi_appointment_request.appointment_request_viewer_group",
            "ssi_appointment_request.appointment_request_user_group",
            "ssi_appointment_request.appointment_request_validator_group",
        ):
            cls.env.ref(xml_id).sudo().write({"users": [(4, cls.admin.id)]})

        Partner = cls.env["res.partner"].with_user(cls.admin)
        cls.company = Partner.create({"name": "Tour HD AP Company", "is_company": True})
        cls.contact = Partner.create(
            {
                "name": "Tour HD AP Contact",
                "parent_id": cls.company.id,
                "type": "contact",
            }
        )

        # Edit tour -- Pre-Condition: a draft ticket and an appointment
        # request that is not linked to it.
        cls.ticket = (
            cls.env["helpdesk_ticket"]
            .with_user(cls.admin)
            .create(
                {
                    "title": "Tour HD AP Edit Ticket",
                    "commercial_partner_id": cls.company.id,
                    "partner_id": cls.contact.id,
                    "date": "2026-01-15",
                }
            )
        )
        cls.appointment_type = cls.env["appointment_type"].create(
            {
                "name": "Tour HD AP Type",
                "code": "TOURHDAP",
                "request_date_offset": 1,
            }
        )
        cls.request = (
            cls.env["appointment_request"]
            .with_user(cls.admin)
            .create(
                {
                    "title": "Tour HD AP Request",
                    "partner_id": cls.contact.id,
                    "type_id": cls.appointment_type.id,
                    "date": "2026-01-15",
                    "date_offset": 1,
                    "appointment_method": "online",
                }
            )
        )

    def test_edit(self):
        """Run the edit tour for the appointment extension.

        IK: docs/helpdesk_ticket/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_helpdesk_appointment_helpdesk_ticket_edit", login="admin"
        )
