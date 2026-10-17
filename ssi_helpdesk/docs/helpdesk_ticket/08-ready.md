# Set Ready Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **State:** `draft` → `ready`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `ready_ok` for state
  `draft` to the actor's group.
- **Access:** User is in group _Helpdesk Ticket / User_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to stage.
3. Click the **Stage** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Ready to Start**.
