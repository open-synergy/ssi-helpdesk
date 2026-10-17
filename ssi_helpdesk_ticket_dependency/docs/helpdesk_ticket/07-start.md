# Start Helpdesk Ticket

> **Module:** `ssi_helpdesk_ticket_dependency`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, aksi `07-start`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_ticket_dependency` is installed.
- **Record:** Every _Finish to Start_ dependency of the ticket has a blocker ticket that
  is **Done**, **Cancelled** or **Terminated**, and every _Start to Start_ dependency
  has a blocker ticket that is already started (**On Progress** or later).

## Modified Flow

- Anchor: after Flow step 4 (_Click OK on the confirmation dialog_), when a dependency
  above is not met, an error dialog names the blocker tickets and their dependency types
  and the ticket stays **Ready to Start**. Click **OK** to close the dialog, satisfy the
  blockers and start the ticket again.

## Additional Post-Condition

- When the dependencies are met, the status changes to **On Progress** as usual.
