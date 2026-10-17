# Delete Helpdesk Data Requirement Type

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_data_requirement_type`\
> **Menu:** Helpdesk > Configuration > Data Requirement Types\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Data Requirement Type`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by a ticket data requirement line.
- **Access:** User is in group
  `Helpdesk - Configurator / Helpdesk Data Requirement Type`.

## Flow

1. Open the **Helpdesk > Configuration > Data Requirement Types** menu.
2. Open the record to delete.
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.
5. Click the **Data Requirement Types** breadcrumb to return to the list.

## Post-Condition

- The record is permanently removed from the system.
- The list view no longer shows the deleted record.
