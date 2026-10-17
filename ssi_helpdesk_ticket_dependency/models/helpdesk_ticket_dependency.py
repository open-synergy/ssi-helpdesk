# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

STARTED_STATES = ("open", "confirm", "done", "cancel", "terminate")
FINISHED_STATES = ("done", "cancel", "terminate")


class HelpdeskTicketDependency(models.Model):
    """Dependency of a helpdesk ticket on a blocker.

    A blocker is either another helpdesk ticket, linked with a project
    management dependency type (finish to start, start to start, finish
    to finish or start to finish), or an external work item that is
    marked as resolved by hand. The ticket cannot be started or
    finished while its blockers are not satisfied.
    """

    _name = "helpdesk_ticket.dependency"
    _description = "Helpdesk Ticket Dependency"
    _order = "sequence, id"

    ticket_id = fields.Many2one(
        string="# Helpdesk Ticket",
        comodel_name="helpdesk_ticket",
        required=True,
        ondelete="cascade",
        help="Ticket that depends on the blocker.",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=10,
        help="Order of the dependency in the ticket.",
    )
    blocker_kind = fields.Selection(
        string="Blocker Kind",
        selection=[
            ("ticket", "Ticket"),
            ("external", "External"),
        ],
        required=True,
        default="ticket",
        help="Whether the blocker is another ticket or an external item.",
    )
    blocker_ticket_id = fields.Many2one(
        string="Blocker Ticket",
        comodel_name="helpdesk_ticket",
        ondelete="restrict",
        help="Ticket that has to reach the required state first.",
    )
    dependency_type = fields.Selection(
        string="Dependency Type",
        selection=[
            ("fs", "Finish to Start"),
            ("ss", "Start to Start"),
            ("ff", "Finish to Finish"),
            ("sf", "Start to Finish"),
        ],
        default="fs",
        help="Finish to Start: this ticket cannot start until the blocker "
        "is finished. Start to Start: this ticket cannot start until the "
        "blocker is started. Finish to Finish: this ticket cannot finish "
        "until the blocker is finished. Start to Finish: this ticket "
        "cannot finish until the blocker is started.",
    )
    external_reference = fields.Char(
        string="External Reference",
        help="Free text reference of the external blocker, for example "
        "owner/repo#N or a URL.",
    )
    external_resolved = fields.Boolean(
        string="External Resolved",
        default=False,
        help="Tick when the external blocker has been resolved.",
    )
    satisfied = fields.Boolean(
        string="Satisfied",
        compute="_compute_satisfied",
        store=True,
        compute_sudo=True,
        help="Checked when the condition of this dependency is met.",
    )

    @api.depends(
        "blocker_kind",
        "dependency_type",
        "external_resolved",
        "blocker_ticket_id.state",
    )
    def _compute_satisfied(self):
        """Compute whether the dependency condition is met."""
        for record in self:
            result = record._evaluate_satisfied()
            record.satisfied = result

    def _evaluate_satisfied(self):
        """Evaluate the dependency condition from the current states.

        An external blocker is met when it is marked as resolved. A
        ticket blocker is met when it is finished (finish to start and
        finish to finish) or started (start to start and start to
        finish). A cancelled or terminated blocker counts as finished.

        :return: True when the condition is met
        :rtype: bool
        """
        self.ensure_one()
        result = True
        if self.blocker_kind == "external":
            result = self.external_resolved
        elif self.blocker_ticket_id:
            state = self.blocker_ticket_id.state
            if self.dependency_type in ("fs", "ff"):
                result = state in FINISHED_STATES
            elif self.dependency_type in ("ss", "sf"):
                result = state in STARTED_STATES
        return result

    def _is_start_gate(self):
        """Tell whether the dependency holds the start of the ticket.

        :return: True for finish to start and start to start rows
        :rtype: bool
        """
        self.ensure_one()
        return self.blocker_kind == "ticket" and self.dependency_type in (
            "fs",
            "ss",
        )

    def _is_finish_gate(self):
        """Tell whether the dependency holds the finish of the ticket.

        :return: True for finish to finish, start to finish and
            external rows
        :rtype: bool
        """
        self.ensure_one()
        return not self._is_start_gate()

    def _get_blocker_label(self):
        """Build the text that names the blocker in error messages.

        :return: ticket number and title, or the external reference
        :rtype: str
        """
        self.ensure_one()
        result = self.external_reference or ""
        if self.blocker_kind == "ticket" and self.blocker_ticket_id:
            blocker = self.blocker_ticket_id
            result = "%s [%s]" % (blocker.name, blocker.title)
        return result

    @api.constrains(
        "blocker_kind",
        "blocker_ticket_id",
        "dependency_type",
        "external_reference",
    )
    def _check_required_blocker_fields(self):
        """Require the fields that match the blocker kind.

        :raises ValidationError: if a ticket blocker has no ticket or
            type, or an external blocker has no reference
        """
        for record in self:
            problem = False
            solution = False
            if record.blocker_kind == "ticket":
                if not record.blocker_ticket_id or not record.dependency_type:
                    problem = _("Blocker ticket and dependency type are required")
                    solution = _("Fill the blocker ticket and the dependency type")
            elif not record.external_reference:
                problem = _("External reference is required")
                solution = _("Fill the external reference")
            if problem:
                error_message = _(
                    """
Context: Validate ticket dependency
Database ID: %s
Problem: %s
Solution: %s
"""
                    % (record.id, problem, solution)
                )
                raise ValidationError(error_message)

    @api.constrains("ticket_id", "blocker_ticket_id")
    def _check_blocker_not_self(self):
        """Forbid a ticket from blocking itself.

        :raises ValidationError: if the blocker is the ticket itself
        """
        for record in self:
            if (
                record.blocker_ticket_id
                and record.blocker_ticket_id == record.ticket_id
            ):
                error_message = _(
                    """
Context: Validate ticket dependency
Database ID: %s
Problem: A ticket cannot depend on itself
Solution: Select another blocker ticket
"""
                    % (record.id,)
                )
                raise ValidationError(error_message)

    @api.constrains("ticket_id", "blocker_ticket_id")
    def _check_unique_pair(self):
        """Forbid the same blocker from being listed twice in a ticket.

        :raises ValidationError: if the (ticket, blocker) pair exists
        """
        for record in self:
            if not record.blocker_ticket_id:
                continue
            criteria = [
                ("ticket_id", "=", record.ticket_id.id),
                ("blocker_ticket_id", "=", record.blocker_ticket_id.id),
                ("id", "!=", record.id),
            ]
            if self.search_count(criteria) > 0:
                error_message = _(
                    """
Context: Validate ticket dependency
Database ID: %s
Problem: Blocker ticket %s is already listed for this ticket
Solution: Remove the duplicated dependency
"""
                    % (record.id, record.blocker_ticket_id.title)
                )
                raise ValidationError(error_message)

    @api.constrains("ticket_id", "blocker_ticket_id")
    def _check_no_cycle(self):
        """Forbid dependency cycles of any length between tickets.

        The blockers of the blocker are followed transitively; the
        dependency is rejected when the ticket itself is reached.

        :raises ValidationError: if the blocker chain leads back to
            the ticket
        """
        for record in self:
            if not record.blocker_ticket_id or not record.ticket_id:
                continue
            if record.blocker_ticket_id == record.ticket_id:
                continue
            if record._reaches_ticket(record.blocker_ticket_id, record.ticket_id):
                error_message = _(
                    """
Context: Validate ticket dependency
Database ID: %s
Problem: Dependency cycle detected between %s and %s
Solution: Remove one of the dependencies that form the cycle
"""
                    % (
                        record.id,
                        record.ticket_id.title,
                        record.blocker_ticket_id.title,
                    )
                )
                raise ValidationError(error_message)

    def _reaches_ticket(self, start, target):
        """Follow blocker tickets from ``start`` looking for ``target``.

        :param start: ticket where the walk starts
        :param target: ticket that closes a cycle when reached
        :return: True when ``target`` is reachable from ``start``
        :rtype: bool
        """
        self.ensure_one()
        result = False
        visited = start.browse()
        pending = start
        while pending and not result:
            visited |= pending
            blockers = pending.dependency_ids.mapped("blocker_ticket_id")
            if target in blockers:
                result = True
            pending = blockers - visited
        return result
