# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools import html_escape

from .helpdesk_resolution_documentation_type import EVIDENCE_KIND_SELECTION


class HelpdeskTicketResolutionDocumentation(models.Model):
    """Resolution documentation line of a helpdesk ticket.

    Records one documentation that must be produced to resolve the
    ticket, optionally typed. The documentation is proven by a
    message, an Odoo record, a decision, a URL or a code reference.
    """

    _name = "helpdesk_ticket.resolution_documentation"
    _description = "Helpdesk Ticket Resolution Documentation"
    _order = "ticket_id, sequence, id"

    ticket_id = fields.Many2one(
        string="# Helpdesk Ticket",
        comodel_name="helpdesk_ticket",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=10,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="helpdesk_resolution_documentation_type",
        ondelete="restrict",
    )
    name = fields.Char(
        string="Documentation",
        required=True,
    )
    url = fields.Char(
        string="URL",
        required=False,
    )
    evidence_kind = fields.Selection(
        string="Evidence Kind",
        selection=EVIDENCE_KIND_SELECTION,
        required=False,
        help="Kind of evidence that proves this documentation. "
        "Leave empty to prove it with the URL only.",
    )
    allowed_message_ids = fields.Many2many(
        string="Allowed Messages",
        comodel_name="mail.message",
        compute="_compute_allowed_message_ids",
        store=False,
        compute_sudo=True,
    )
    message_id = fields.Many2one(
        string="Message",
        comodel_name="mail.message",
        ondelete="set null",
        domain="[('id', 'in', allowed_message_ids)]",
        help="Email or comment of the ticket or of one of its "
        "communications that proves this documentation.",
    )
    evidence_record_ref = fields.Reference(
        string="Odoo Record",
        selection="_selection_evidence_record_ref",
        help="Odoo record that proves this documentation.",
    )
    decision_note = fields.Text(
        string="Decision",
        help="Decision that proves this documentation.",
    )
    evidence_date = fields.Date(
        string="Evidence Date",
        compute="_compute_evidence_date",
        store=True,
        readonly=False,
        compute_sudo=True,
        help="Date of the evidence. It follows the message date for "
        "message evidence, and is filled manually otherwise.",
    )
    evidence_partner_id = fields.Many2one(
        string="Confirmed By",
        comodel_name="res.partner",
        related="message_id.author_id",
        store=True,
        compute_sudo=True,
        help="Author of the evidence message.",
    )
    evidence_channel_id = fields.Many2one(
        string="Evidence Channel",
        comodel_name="helpdesk_channel",
        compute="_compute_evidence_channel_id",
        store=True,
        compute_sudo=True,
        help="Channel of the communication that holds the evidence " "message.",
    )
    root_cause_id = fields.Many2one(
        string="Root Cause",
        comodel_name="helpdesk_root_cause",
        ondelete="restrict",
        help="Root cause of the ticket problem. It is required to "
        "complete a documentation whose type requires a root cause.",
    )
    root_cause_note = fields.Text(
        string="Root Cause Note",
        help="Explanation of the root cause.",
    )
    required_evidence_kind = fields.Selection(
        string="Required Evidence Kind",
        related="type_id.required_evidence_kind",
        store=False,
        compute_sudo=True,
    )
    requires_customer_confirmation = fields.Boolean(
        string="Requires Customer Confirmation",
        related="type_id.requires_customer_confirmation",
        store=False,
        compute_sudo=True,
    )
    third_party = fields.Boolean(
        string="Third Party",
        related="type_id.third_party",
        store=False,
        compute_sudo=True,
    )
    requires_root_cause = fields.Boolean(
        string="Requires Root Cause",
        related="type_id.requires_root_cause",
        store=False,
        compute_sudo=True,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("open", "In Progress"),
            ("done", "Done"),
        ],
        compute="_compute_state",
        store=True,
        compute_sudo=True,
    )

    @api.model
    def _selection_evidence_record_ref(self):
        """Return the models that can be referenced as evidence.

        :return: list of (model name, model label) of non-transient
            models
        """
        models = self.env["ir.model"].sudo().search([("transient", "=", False)])
        return [(model.model, model.name) for model in models]

    @api.depends(
        "ticket_id",
        "ticket_id.communication_ids",
    )
    def _compute_allowed_message_ids(self):
        """Compute the messages that can be chosen as evidence.

        The allowed messages are the email and comment messages of the
        ticket and of its communications.
        """
        Message = self.env["mail.message"]
        for record in self:
            result = Message
            ticket = record.ticket_id or self.env["helpdesk_ticket"].browse(
                self.env.context.get("default_ticket_id")
            )
            if ticket:
                criteria = [
                    ("message_type", "in", ["email", "comment"]),
                    "|",
                    "&",
                    ("model", "=", "helpdesk_ticket"),
                    ("res_id", "=", ticket.id),
                    "&",
                    ("model", "=", "helpdesk_communication"),
                    ("res_id", "in", ticket.communication_ids.ids),
                ]
                result = Message.search(criteria)
            record.allowed_message_ids = result

    @api.depends(
        "evidence_kind",
        "message_id",
    )
    def _compute_evidence_date(self):
        """Compute the evidence date from the evidence message.

        For message evidence the date is the message date. In the
        other cases the current value is kept, so it can be filled
        manually.
        """
        for record in self:
            result = record.evidence_date
            if record.evidence_kind == "message" and record.message_id:
                result = fields.Datetime.to_datetime(record.message_id.date).date()
            record.evidence_date = result

    @api.depends(
        "message_id",
        "message_id.model",
        "message_id.res_id",
    )
    def _compute_evidence_channel_id(self):
        """Compute the channel of the evidence message.

        The channel is the channel of the communication that holds the
        message, and empty when the message belongs to another record.
        """
        Communication = self.env["helpdesk_communication"]
        for record in self:
            result = False
            message = record.message_id
            if message and message.model == "helpdesk_communication":
                result = Communication.browse(message.res_id).channel_id
            record.evidence_channel_id = result

    @api.depends(
        "url",
        "evidence_kind",
        "message_id",
        "evidence_partner_id",
        "evidence_record_ref",
        "decision_note",
        "root_cause_id",
        "type_id",
        "type_id.required_evidence_kind",
        "type_id.requires_customer_confirmation",
        "type_id.requires_root_cause",
    )
    def _compute_state(self):
        """Compute the state of the documentation.

        The state is ``done`` once the evidence valid for the evidence
        kind is filled: the message, the Odoo record, the decision
        note, or the URL for the url and code kinds. When the kind is
        empty the URL alone proves the documentation, which keeps the
        behavior of the lines created before the kind existed.

        The type adds requirements. The evidence kind must be the
        required one of the type. A type that requires customer
        confirmation needs a message kind evidence whose author is not
        a partner of a company. A type that requires a root cause needs
        the root cause to be filled. Otherwise the state is ``open``.
        """
        company_partners = (
            self.env["res.company"].sudo().search([]).mapped("partner_id")
        )
        for record in self:
            kind = record.evidence_kind
            proof = {
                "message": record.message_id,
                "record": record.evidence_record_ref,
                "decision": record.decision_note,
                "url": record.url,
                "code": record.url,
            }.get(kind, record.url)
            valid = bool(proof)
            doc_type = record.type_id
            if valid and doc_type.required_evidence_kind:
                valid = kind == doc_type.required_evidence_kind
            if valid and doc_type.requires_customer_confirmation:
                valid = (
                    kind == "message"
                    and bool(record.message_id)
                    and bool(record.evidence_partner_id)
                    and record.evidence_partner_id not in company_partners
                )
            if valid and doc_type.requires_root_cause:
                valid = bool(record.root_cause_id)
            result = "open"
            if valid:
                result = "done"
            record.state = result

    def _get_evidence_summary(self):
        """Return a readable summary of the current evidence.

        :return: text with the evidence kind and its reference
        """
        self.ensure_one()
        kind_labels = dict(self._fields["evidence_kind"].selection)
        parts = []
        if self.evidence_kind:
            parts.append(kind_labels[self.evidence_kind])
        if self.message_id:
            parts.append("message #%s" % self.message_id.id)
        if self.evidence_record_ref:
            parts.append(
                "%s (%s)"
                % (
                    self.evidence_record_ref.sudo().display_name,
                    self.evidence_record_ref._name,
                )
            )
        if self.decision_note:
            parts.append(self.decision_note)
        if self.url:
            parts.append(self.url)
        if self.evidence_date:
            parts.append(str(self.evidence_date))
        return ", ".join(parts) or "-"

    def write(self, vals):
        """Write the lines and log evidence changes on the ticket.

        When one of the evidence fields changes, a note with the old
        and new evidence is posted on the ticket chatter.

        :param vals: dict of field values
        :return: result of the parent write
        """
        evidence_fields = {
            "evidence_kind",
            "message_id",
            "evidence_record_ref",
            "decision_note",
            "url",
            "evidence_date",
        }
        track = bool(evidence_fields & set(vals))
        old = {}
        if track:
            old = {record.id: record._get_evidence_summary() for record in self}
        result = super().write(vals)
        if track:
            for record in self:
                new = record._get_evidence_summary()
                if new != old[record.id]:
                    record._log_evidence_change(old[record.id], new)
        return result

    def _log_evidence_change(self, old, new):
        """Post a note on the ticket about an evidence change.

        :param old: summary of the previous evidence
        :param new: summary of the new evidence
        """
        self.ensure_one()
        body = "<p>Resolution documentation <b>%s</b>: %s &rarr; %s</p>" % (
            html_escape(self.name or ""),
            html_escape(old),
            html_escape(new),
        )
        self.ticket_id.message_post(
            body=body,
            message_type="comment",
            subtype_xmlid="mail.mt_note",
        )

    @api.onchange(
        "type_id",
    )
    def onchange_name(self):
        """Fill the documentation name from the selected type.

        The name is the type name, or empty when no type is selected.
        """
        self.name = False
        if self.type_id:
            self.name = self.type_id.name

    @api.onchange(
        "type_id",
    )
    def onchange_evidence_kind(self):
        """Fill the evidence kind from the required one of the type.

        The kind is set only when the selected type requires one, so
        the current kind is kept otherwise.
        """
        if self.type_id.required_evidence_kind:
            self.evidence_kind = self.type_id.required_evidence_kind
