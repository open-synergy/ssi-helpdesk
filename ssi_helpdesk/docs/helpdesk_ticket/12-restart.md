# Restart Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / Validator`\
> **State:** `cancel` or `reject` → `draft`\
> **Requires:** `10-cancel`

## Pre-Condition

- **Record:** Status is **Cancelled** or **Rejected**.
- **Config:** An active `policy.template` for this model grants `restart_ok` for states
  `cancel` and `reject` to the actor's group.
- **Access:** User is in group _Helpdesk Ticket / Validator_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. The default list filters hide cancelled tickets. Open the **Filters** menu and select
   **Cancel** so that cancelled tickets are listed.
3. Open the record to restart.
4. Click the **Restart** button.
5. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Draft**.
