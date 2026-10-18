# Activate Helpdesk Root Cause

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_root_cause`\
> **Menu:** Helpdesk > Configuration > Ticket > Root Causes\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Root Cause`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Helpdesk - Configurator / Helpdesk Root Cause`.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Root Causes** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The root causes can be selected again as **Root Cause** on a new ticket resolution
  documentation line.
