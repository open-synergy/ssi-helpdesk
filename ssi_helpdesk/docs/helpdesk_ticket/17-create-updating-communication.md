# Create Updating Communication from Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft** or **On Progress**.
- **Access:** User is in group _Helpdesk Ticket / User_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to report on.
3. Open the **Communications** tab.
4. Click the **Updating** button.

## Post-Condition

- A new communication is created in **Draft** status, titled _Ticket status update_
  followed by the ticket number and today's date, and linked to the ticket. Its form is
  displayed. The ticket contact and the **CC To** contacts are subscribed to it.
- Unlike the finishing communication, it is not stored on the ticket, so the button
  stays available and can be used again.
