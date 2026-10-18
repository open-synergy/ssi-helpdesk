# Confirm Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **State:** `open` → `confirm`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for this model grants `confirm_ok` for state
  `open` to the actor's group.
- **Config:** An active `approval.template` for this model matches this record and has
  at least one approver level.
- **Record:** Every ticket split from this one is **Done**, **Cancelled** or
  **Terminated**; a ticket split from it that is still in progress blocks the
  confirmation.
- **Record:** Every communication of this ticket, other than its finishing
  communication, is **Done**; a communication that is still **Draft** or **Open** blocks
  the confirmation.
- **Access:** User is in group _Helpdesk Ticket / User_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the approval template.
