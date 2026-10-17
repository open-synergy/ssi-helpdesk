# Create Ticket From Helpdesk Communication

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_communication`\
> **Menu:** Helpdesk > Communications\
> **Actor:** user in groups `Helpdesk Communication / User` and `Helpdesk Ticket / User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The **# Ticket** field is empty. The **Create Ticket** button is hidden
  once a ticket is linked.
- **Data:** A ticket category exists, and at least one ticket type belongs to it.
- **Access:** User is in groups _Helpdesk Communication / User_ and _Helpdesk Ticket /
  User_.

## Flow

1. Open the **Helpdesk > Communications** menu.
2. Open the record to convert into a ticket.
3. Click the **Create Ticket** button.
4. In the wizard that appears, fill in the required fields:
   - **Category** _(required)_: Select the ticket category.
   - **Type** _(required)_: Select the ticket type. Available options are the types of
     the selected **Category**. Changing the **Category** clears this field, so select
     the **Category** first.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- A new ticket is created in **Draft** status and opened. It takes the **Contact**,
  **Commercial Contact**, **Date** and **Title** of the communication, plus the selected
  **Category** and **Type**; its duration and deadline follow the selected **Type**.
- The communication is linked to the new ticket (**# Ticket**), and is the ticket's **#
  Starting Communication**.
