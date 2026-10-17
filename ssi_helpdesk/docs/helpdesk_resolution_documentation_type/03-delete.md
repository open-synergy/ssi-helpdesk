# Delete Helpdesk Resolution Documentation Type

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_resolution_documentation_type`\
> **Menu:** Helpdesk > Configuration > Ticket > Resolution Documentation Types\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Resolution Documentation Type`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by a ticket resolution documentation line.
- **Access:** User is in group
  `Helpdesk - Configurator / Helpdesk Resolution Documentation Type`.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Resolution Documentation Types** menu.
2. Open the record to delete.
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.
5. Click the **Resolution Documentation Types** breadcrumb to return to the list.

## Post-Condition

- The record is permanently removed from the system.
- The list view no longer shows the deleted record.
