# Reload Followers Helpdesk Communication

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_communication`\
> **Menu:** Helpdesk > Communications\
> **Actor:** user in group `Helpdesk Communication / User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The **# Ticket** field is filled. The **Reload Followers From Ticket**
  button is hidden while it is empty.
- **Data:** The linked ticket has a **Responsible**, a **Contact** and, optionally,
  additional contacts.
- **Access:** User is in group _Helpdesk Communication / User_.

## Flow

1. Open the **Helpdesk > Communications** menu.
2. Open the record whose followers will be reloaded.
3. Click the **Reload Followers From Ticket** button.

## Post-Condition

- The followers of the communication now also include the **Responsible**, the
  **Contact** and the additional contacts of the linked ticket.
- Existing followers are kept; nobody is removed.
