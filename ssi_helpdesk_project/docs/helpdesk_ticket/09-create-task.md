# Create Task from Helpdesk Ticket

> **Module:** `ssi_helpdesk_project`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group _Helpdesk Ticket / User_\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The ticket is saved and has a **Project** selected on the **Tasks** tab.
- **Data:** The ticket **Type** has at least one task template on its **Project** tab.
- **Access:** User is in group _Helpdesk Ticket / User_.
- **Module:** `ssi_helpdesk_project` is installed.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Find and open the ticket.
3. Open the **Tasks** tab.
4. Click the **Create** button.

## Post-Condition

- One project task is created in the ticket **Project** for every task template of the
  ticket **Type**, named after its **Task Summary**.
- The created tasks are linked to the ticket and listed on the **Tasks** tab.
- Nothing is created when the ticket has no **Project** selected.
