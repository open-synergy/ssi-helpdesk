# Deactivate Helpdesk Data Requirement Type

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_data_requirement_type`\
> **Menu:** Helpdesk > Configuration > Data Requirement Types\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Data Requirement Type`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group
  `Helpdesk - Configurator / Helpdesk Data Requirement Type`.

## Flow

1. Open the **Helpdesk > Configuration > Data Requirement Types** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated types cannot be selected as **Type** on a new ticket data requirement
  line.
- Existing lines that already use a deactivated type can still be viewed.
