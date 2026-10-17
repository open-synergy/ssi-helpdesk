# Activate Helpdesk Type

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_type`
>
> **Menu:** Helpdesk > Configuration > Ticket > Types
>
> **Actor:** user in group _Helpdesk Type_
>
> **Active:** `false` → `true`
>
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group _Helpdesk Type_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Types** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected as the **Type** of a new `helpdesk_ticket`.
