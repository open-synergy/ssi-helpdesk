# Reject Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** approver on the pending approval level (group `Helpdesk Ticket / Validator`
> in the standard approval template)\
> **State:** `confirm` → `reject`\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` for this model grants `reject_ok` for state
  `confirm` to approvers on the pending level.
- **Access:** User is registered as an approver on the approval level that is currently
  pending.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to reject.
3. Click the **Reject** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Rejected**.
