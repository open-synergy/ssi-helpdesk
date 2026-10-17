# Activate Helpdesk Channel

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_channel`
>
> **Menu:** Helpdesk ‣ Configuration ‣ Communication ‣ Channels
>
> **Actor:** user in group `Helpdesk Channel`
>
> **Active:** `false` → `true`
>
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Helpdesk Channel`.

## Flow

1. Open the **Helpdesk ‣ Configuration ‣ Communication ‣ Channels** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** ‣ **Unarchive**.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected on new Helpdesk Communication records.
