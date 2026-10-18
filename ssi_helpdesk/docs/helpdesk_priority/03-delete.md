# Delete Helpdesk Priority

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_priority`
>
> **Menu:** Helpdesk > Configuration > Ticket > Priorities
>
> **Actor:** user in group _Helpdesk Priority_
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by a `helpdesk_ticket`.
- **Access:** User is in group _Helpdesk Priority_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Priorities** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
