# Deactivate Helpdesk Resolution Documentation Type

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_resolution_documentation_type`\
> **Menu:** Helpdesk > Configuration > Ticket > Resolution Documentation Types\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Resolution Documentation Type`\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group
  `Helpdesk - Configurator / Helpdesk Resolution Documentation Type`.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Resolution Documentation Types** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated types cannot be selected as **Type** on a new ticket resolution
  documentation line.
- Existing lines that already use a deactivated type can still be viewed.
