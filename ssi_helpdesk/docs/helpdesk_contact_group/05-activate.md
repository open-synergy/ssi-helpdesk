# Activate Helpdesk Contact Group

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_contact_group`
>
> **Menu:** Helpdesk ‣ Configuration ‣ Ticket ‣ Contact Groups
>
> **Actor:** user in group `Helpdesk Contact Group`
>
> **Active:** `false` → `true`
>
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Helpdesk Contact Group`.

## Flow

1. Open the **Helpdesk ‣ Configuration ‣ Ticket ‣ Contact Groups** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** ‣ **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected on new Helpdesk Ticket records.
