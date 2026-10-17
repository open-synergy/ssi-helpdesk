# Split Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** A ticket exists. The **Split Ticket** button is available in every status.
- **Data:** A ticket category and a ticket type that belongs to that category exist.
- **Access:** User is in group _Helpdesk Ticket / User_ (the group allowed to use the
  split wizard).

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to split.
3. Open the **Duplicate & Split** tab.
4. Click the **Split Ticket** button.
5. In the wizard that appears, fill in the fields:
   - **Title** _(required)_: Enter the title of the new ticket.
   - **Category** _(required)_: Select the category of the new ticket. Changing the
     **Category** clears **Type**.
   - **Type** _(required)_: Select the type of the new ticket. Available options are
     based on **Category**.
   - **Description**: Optionally describe the new ticket.
6. Click **Confirm** on the wizard.
7. Click **OK** on the confirmation dialog.

## Post-Condition

- A new ticket is created as a copy of the original one, with the **Title**,
  **Category** and **Type** entered in the wizard, and its form is displayed.
- The new ticket refers to the original one in **# Original Ticket**, and the original
  ticket lists it under **Split Into**.

## Related Views

- The **Open Split Result(s)** button (`action_open_split`) opens the list of tickets
  created by splitting the current ticket. It only navigates to that list — it does not
  write any field or change state, so it has no work instruction or tour of its own.
