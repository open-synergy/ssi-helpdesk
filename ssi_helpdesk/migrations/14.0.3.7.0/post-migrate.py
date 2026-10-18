# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Migration: 14.0.3.6.0 -> 14.0.3.7.0
#
# Changes: helpdesk_ticket gained the required ``priority_id`` field.
#          The column is created without a value for existing tickets
#          because the default (the Medium priority record) is only
#          loaded after the column is created, so Odoo cannot fill it
#          nor set NOT NULL on it.
#
#          This script gives every existing ticket the Medium
#          priority, then enforces NOT NULL on the column. The
#          default priority of the ticket type is not used: the new
#          ``helpdesk_type.priority_id`` is empty on every type when
#          this script runs.

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    """Set the Medium priority on tickets that have no priority.

    :param env: Odoo environment
    :param version: previously installed module version
    """
    medium = env.ref(
        "ssi_helpdesk.helpdesk_priority_medium",
        raise_if_not_found=False,
    )
    if not medium:
        _logger.warning(
            "Medium priority not found; existing tickets are left " "without priority."
        )
        return
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE helpdesk_ticket
        SET priority_id = %s
        WHERE priority_id IS NULL
        """,
        (medium.id,),
    )
    openupgrade.logged_query(
        env.cr,
        "ALTER TABLE helpdesk_ticket ALTER COLUMN priority_id SET NOT NULL",
    )
