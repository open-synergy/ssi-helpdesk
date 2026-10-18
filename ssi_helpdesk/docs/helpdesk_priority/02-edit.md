# Edit Helpdesk Priority

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

- **Record:** The record is active.
- **Access:** User is in group _Helpdesk Priority_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Priorities** menu.
2. Find and open the record to edit.
3. Change the required fields.
4. Click **Save**.

To reorder priorities without opening a record, drag the handle at the start of a row in
the list view; the **Sequence** values are updated automatically.

## Post-Condition

- The record is updated with the new values.
