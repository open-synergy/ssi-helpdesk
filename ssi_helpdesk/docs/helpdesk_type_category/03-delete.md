# Delete Helpdesk Type Category

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_type_category`
>
> **Menu:** Helpdesk > Configuration > Ticket > Categories
>
> **Actor:** user in group _Helpdesk Type Category_
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is not referenced by a `helpdesk_type` or a `helpdesk_ticket`.
- **Access:** User is in group _Helpdesk Type Category_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Categories** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.

## Post-Condition

- The selected records are permanently removed from the system.
