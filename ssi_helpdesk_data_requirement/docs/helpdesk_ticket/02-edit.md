# Edit Helpdesk Ticket

> **Module:** `ssi_helpdesk_data_requirement`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, aksi `02-edit`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_data_requirement` is installed.

## Modified Flow

- Anchor: after Flow step 2 (_Find and open the record to edit_), the ticket form shows
  a **Data Requirements** tab.
- Open the **Data Requirements** tab to see the **Allowed Partner** and **Data
  Requirement Status** fields and the list of data requirements linked to the ticket.
- Use the tab buttons **Open Data Requirements**, **Create Data Requirements**, and
  **Add Data Requirements** to review or extend the data requirements of the ticket. The
  data requirements are taken from the ticket type, so the type needs lines in its
  **Data Requirements** tab.

## Additional Post-Condition

- The **Data Requirement Status** field shows **Not Needed** when the ticket has no data
  requirement, **In Progress** while some are not done, and **Done** when all are done.
