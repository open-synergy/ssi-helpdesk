# Restart Helpdesk Communication

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_communication`\
> **Menu:** Helpdesk > Communications\
> **Actor:** user in group `Helpdesk Communication / Validator`\
> **State:** `open` → `draft`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Config:** An active `policy.template` for this model grants `restart_ok` for state
  `open` to the actor's group.
- **Access:** User is in group _Helpdesk Communication / Validator_.

## Flow

1. Open the **Helpdesk > Communications** menu.
2. Open the record to restart.
3. Click the **Restart** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status returns to **Draft**.
- The same transition also happens automatically, without any button click, when the
  contact replies and the record no longer waits for a response (the **Waiting for
  Respon** field turns off).
