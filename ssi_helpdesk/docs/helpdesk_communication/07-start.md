# Start Helpdesk Communication

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_communication`\
> **Menu:** Helpdesk > Communications\
> **Actor:** user in group `Helpdesk Communication / User`\
> **State:** `draft` → `open`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `open_ok` for state
  `draft` to the actor's group.
- **Access:** User is in group _Helpdesk Communication / User_.

## Flow

1. Open the **Helpdesk > Communications** menu.
2. Open the record to start.
3. Click the **Start** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **On Progress**.
- The communication is now waiting for a response.
- The same transition also happens automatically, without any button click, when the
  latest message on the record is from the company and has no later reply from the
  contact (the **Waiting for Respon** field turns on).
