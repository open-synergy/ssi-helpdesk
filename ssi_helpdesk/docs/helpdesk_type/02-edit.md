# Edit Helpdesk Type

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_type`
>
> **Menu:** Helpdesk > Configuration > Ticket > Types
>
> **Actor:** user in group _Helpdesk Type_
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is active.
- **Access:** User is in group _Helpdesk Type_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Types** menu.
2. Find and open the record to edit.
3. Change the required fields, including the optional **Default Priority**.
4. Optionally, on the **Resolution Documentation(s)** tab, maintain the required
   documentations of the type:
   - Click **Add a line** and select the **Documentation Type** _(required)_. The
     **Documentation** name is filled from the type. Change if needed.
   - Change **Sequence** by dragging the handle.
   - Remove a line with the delete icon. Only required documentations belong here.
     Tickets of this type receive these lines when the type is selected.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- The required documentation lines are saved on the **Resolution Documentation(s)** tab.
