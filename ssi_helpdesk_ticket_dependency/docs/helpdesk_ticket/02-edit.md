# Edit Helpdesk Ticket

> **Module:** `ssi_helpdesk_ticket_dependency`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, aksi `02-edit`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_ticket_dependency` is installed.

## Modified Flow

- Anchor: after Flow step 2 (_Find and open the record to edit_), the ticket form shows
  a **Dependencies** tab.
- Open the **Dependencies** tab to see the **Start Blocked** and **Finish Blocked**
  fields, the list of dependencies of the ticket, and the list of tickets that wait for
  this ticket.
- Add a dependency with **Add a line** and choose the **Blocker Kind**:
  - **Ticket**: select the **Blocker Ticket** and the **Dependency Type** (Finish to
    Start, Start to Start, Finish to Finish or Start to Finish).
  - **External**: type the **External Reference** (for example `owner/repo#12` or a URL)
    and tick **External Resolved** once the work outside Odoo is finished.
- A ticket cannot depend on itself, list the same blocker twice, or form a cycle with
  other tickets; the form shows an error and the line is not saved.

## Additional Post-Condition

- The **Satisfied** column of each line is ticked when its condition is met.
- A **Blocked** badge appears on the ticket form while any dependency is not satisfied,
  and the ticket is found by the **Blocked** filter of the ticket search.
