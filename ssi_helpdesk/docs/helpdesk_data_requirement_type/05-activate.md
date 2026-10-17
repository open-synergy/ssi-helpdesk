# Activate Helpdesk Data Requirement Type

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_data_requirement_type`\
> **Menu:** Helpdesk > Configuration > Data Requirement Types\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Data Requirement Type`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group
  `Helpdesk - Configurator / Helpdesk Data Requirement Type`.

## Flow

1. Open the **Helpdesk > Configuration > Data Requirement Types** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The types can be selected again as **Type** on a new ticket data requirement line.
