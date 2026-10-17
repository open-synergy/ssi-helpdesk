# Delete Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Record:** Document number is **/**. A ticket receives its number automatically when
  it is created, so first reset it: a user in group _Helpdesk Ticket / Validator_ (the
  group granted `manual_number_ok`) opens the Draft record and clicks **Reset Document
  Number**, then **OK** on the confirmation dialog.
- **Access:** User is in group _Helpdesk Ticket / User_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Select one or more records to delete (check the checkbox).
3. Click **Action** > **Delete**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The selected records are permanently removed from the system.
