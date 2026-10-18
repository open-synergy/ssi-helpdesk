# Deactivate Helpdesk Priority

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_priority`
>
> **Menu:** Helpdesk > Configuration > Ticket > Priorities
>
> **Actor:** user in group _Helpdesk Priority_
>
> **Active:** `true` → `false`
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group _Helpdesk Priority_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Priorities** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated records cannot be selected as the **Priority** of a new `helpdesk_ticket`.
- Records that already use this one can still be viewed.
