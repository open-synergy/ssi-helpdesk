# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# Migration: 14.0.3.7.1 -> 14.0.3.7.2
#
# Changes: helpdesk_communication.need_respon, latest_message_id and
#          latest_partner_message_id are now computed together by
#          ``_compute_need_respon``. Previously ``need_respon`` was
#          computed by a separate method, so it was derived from stale
#          sources and many rows stored a wrong value.
#
#          The compute logic changed on columns that already exist, so
#          the stored values of existing rows do not follow by
#          themselves. This script recomputes all three fields.
#
#          The ``base.automation`` rules on ``need_respon`` are
#          registered after "post" migrations, so they do not fire for
#          the corrected values. Communications whose state does not
#          match ``need_respon`` are only counted in the log; their
#          state is not changed.

import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)

GROUP = ["latest_message_id", "latest_partner_message_id", "need_respon"]


@openupgrade.migrate()
def migrate(env, version):
    """Recompute the response fields and log state mismatches.

    :param env: Odoo environment
    :param version: previously installed module version
    """
    records = env["helpdesk_communication"].with_context(active_test=False).search([])
    for name in GROUP:
        env.add_to_compute(records._fields[name], records)
    records.flush(GROUP)
    _logger.info("Recomputed %s on %s record(s).", GROUP, len(records))

    draft_waiting = records.filtered(lambda r: r.state == "draft" and r.need_respon)
    open_not_waiting = records.filtered(
        lambda r: r.state == "open" and not r.need_respon
    )
    _logger.info(
        "State mismatches left untouched: %s draft record(s) with "
        "need_respon=True, %s open record(s) with need_respon=False.",
        len(draft_waiting),
        len(open_not_waiting),
    )
