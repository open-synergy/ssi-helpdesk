# Delete Helpdesk Root Cause

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_root_cause`\
> **Menu:** Helpdesk > Configuration > Ticket > Root Causes\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Root Cause`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by a ticket resolution documentation line.
- **Access:** User is in group `Helpdesk - Configurator / Helpdesk Root Cause`.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Root Causes** menu.
2. Open the record to delete.
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.
5. Click the **Root Causes** breadcrumb to return to the list.

## Post-Condition

- The record is permanently removed from the system.
- The list view no longer shows the deleted record.
