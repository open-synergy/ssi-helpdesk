# Start Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **State:** `ready` → `open`\
> **Requires:** `08-ready`

## Pre-Condition

- **Record:** Status is **Ready to Start**.
- **Config:** An active `policy.template` for this model grants `open_ok` for state
  `ready` to the actor's group.
- **Access:** User is in group _Helpdesk Ticket / User_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to start.
3. Click the **Start** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **On Progress**.
