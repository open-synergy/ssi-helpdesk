# Deactivate Helpdesk Root Cause

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_root_cause`\
> **Menu:** Helpdesk > Configuration > Ticket > Root Causes\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Root Cause`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Helpdesk - Configurator / Helpdesk Root Cause`.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Root Causes** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated root causes cannot be selected as **Root Cause** on a new ticket
  resolution documentation line.
- Existing lines that already use a deactivated root cause can still be viewed.
