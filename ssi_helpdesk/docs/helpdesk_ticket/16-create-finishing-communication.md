# Create Finishing Communication from Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress**.
- **Record:** The ticket has no **Finishing Communication** yet. The button is hidden
  once one has been created.
- **Access:** User is in group _Helpdesk Ticket / User_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to finish.
3. Open the **Communications** tab.
4. Click the **Finishing** button.

## Post-Condition

- A new communication is created in **Draft** status, titled like the ticket and linked
  to it, and its form is displayed. The ticket contact and the **CC To** contacts are
  subscribed to it.
- The new communication is stored in the **Finishing Communication** field of the
  ticket, and the **Finishing** button is hidden from then on.
