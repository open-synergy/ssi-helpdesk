# Deactivate Helpdesk Type Category

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_type_category`
>
> **Menu:** Helpdesk > Configuration > Ticket > Categories
>
> **Actor:** user in group _Helpdesk Type Category_
>
> **Active:** `true` → `false`
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group _Helpdesk Type Category_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Categories** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated records cannot be selected as the **Category** of a new `helpdesk_type` or
  `helpdesk_ticket`.
- Records that already use this one can still be viewed.
