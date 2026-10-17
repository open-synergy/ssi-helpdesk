# Deactivate Helpdesk Channel

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_channel`
>
> **Menu:** Helpdesk ‣ Configuration ‣ Communication ‣ Channels
>
> **Actor:** user in group `Helpdesk Channel`
>
> **Active:** `true` → `false`
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Helpdesk Channel`.

## Flow

1. Open the **Helpdesk ‣ Configuration ‣ Communication ‣ Channels** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** ‣ **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated records cannot be selected on new Helpdesk Communication records.
- Helpdesk Communication records that already use this record can still be viewed.
