# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError

from odoo.addons.ssi_decorator import ssi_decorator


class HelpdeskTicket(models.Model):
    # Extension of helpdesk_ticket: typed dependencies on other tickets
    # or external items that hold the start and the finish of the ticket.
    _inherit = "helpdesk_ticket"

    dependency_ids = fields.One2many(
        string="Dependencies",
        comodel_name="helpdesk_ticket.dependency",
        inverse_name="ticket_id",
        help="Blockers that this ticket depends on.",
    )
    blocking_ids = fields.One2many(
        string="Blocking",
        comodel_name="helpdesk_ticket.dependency",
        inverse_name="blocker_ticket_id",
        readonly=True,
        help="Dependencies of other tickets that wait for this ticket.",
    )
    start_blocked = fields.Boolean(
        string="Start Blocked",
        compute="_compute_blocked",
        store=True,
        compute_sudo=True,
        help="Checked when a dependency still holds the start of the ticket.",
    )
    finish_blocked = fields.Boolean(
        string="Finish Blocked",
        compute="_compute_blocked",
        store=True,
        compute_sudo=True,
        help="Checked when a dependency still holds the finish of the ticket.",
    )
    blocked = fields.Boolean(
        string="Blocked",
        compute="_compute_blocked",
        store=True,
        compute_sudo=True,
        help="Checked when the start or the finish of the ticket is held.",
    )

    @api.depends(
        "dependency_ids.satisfied",
        "dependency_ids.blocker_kind",
        "dependency_ids.dependency_type",
        "dependency_ids.blocker_ticket_id.state",
    )
    def _compute_blocked(self):
        """Compute the blocked flags from the unsatisfied dependencies.

        ``start_blocked`` is set when an unsatisfied dependency holds
        the start, ``finish_blocked`` when one holds the finish, and
        ``blocked`` when either is set.
        """
        for record in self:
            start_result = False
            finish_result = False
            for dependency in record.dependency_ids.filtered(lambda x: not x.satisfied):
                if dependency._is_start_gate():
                    start_result = True
                else:
                    finish_result = True
            record.start_blocked = start_result
            record.finish_blocked = finish_result
            record.blocked = start_result or finish_result

    @ssi_decorator.pre_open_check()
    def _10_check_dependency_on_open(self):
        """Block the start while a start dependency is not satisfied.

        :raises UserError: if a finish to start or start to start
            dependency is still unsatisfied
        """
        self.ensure_one()
        self._check_dependency_gate("Start Ticket", "start")

    @ssi_decorator.pre_confirm_check()
    def _10_check_dependency_on_confirm(self):
        """Block the confirmation while a finish dependency is open.

        :raises UserError: if a finish to finish, start to finish or
            external dependency is still unsatisfied
        """
        self.ensure_one()
        self._check_dependency_gate("Confirm Ticket", "finish")

    @ssi_decorator.pre_done_check()
    def _10_check_dependency_on_done(self):
        """Block the completion while a finish dependency is open.

        :raises UserError: if a finish to finish, start to finish or
            external dependency is still unsatisfied
        """
        self.ensure_one()
        self._check_dependency_gate("Finish Ticket", "finish")

    def _check_dependency_gate(self, context, gate):
        """Ensure the dependencies of one gate are satisfied.

        :param str context: operation name shown in the error message
        :param str gate: ``start`` or ``finish``
        :raises UserError: naming the blockers that are not satisfied
        """
        self.ensure_one()
        unsatisfied = self.dependency_ids.filtered(
            lambda x: not x._evaluate_satisfied()
            and (x._is_start_gate() if gate == "start" else x._is_finish_gate())
        )
        if unsatisfied:
            selection = dict(
                self.env["helpdesk_ticket.dependency"]
                ._fields["dependency_type"]
                .selection
            )
            lines = []
            for dependency in unsatisfied:
                if dependency.blocker_kind == "external":
                    kind = _("External")
                else:
                    kind = selection.get(dependency.dependency_type, "")
                lines.append("%s (%s)" % (dependency._get_blocker_label(), kind))
            error_message = _(
                """
Context: %s
Database ID: %s
Problem: Ticket is blocked by unsatisfied dependencies: %s
Solution: Satisfy the blockers or remove the dependencies first
"""
                % (context, self.id, ", ".join(lines))
            )
            raise UserError(error_message)
