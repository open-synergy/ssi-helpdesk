# Cancel Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / Validator`\
> **State:** `draft`, `ready`, `open`, `confirm` or `done` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**, **Ready to Start**, **On Progress**, **Waiting for
  Approval** or **Done**.
- **Data:** At least one cancel reason is available to this model (a cancel reason
  marked for global use, or one linked to the _Helpdesk Ticket_ model).
- **Config:** An active `policy.template` for this model grants `cancel_ok` for the
  states above to the actor's group.
- **Access:** User is in group _Helpdesk Ticket / Validator_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Reason**.
5. Click **Confirm** on the wizard.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
- The selected reason is shown on the form as **Cancellation reason**.
