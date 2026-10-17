# Confirm Helpdesk Ticket

> **Module:** `ssi_helpdesk_ticket_dependency`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, aksi `04-confirm`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_ticket_dependency` is installed.
- **Record:** Every _Finish to Finish_ dependency has a blocker ticket that is **Done**,
  **Cancelled** or **Terminated**, every _Start to Finish_ dependency has a blocker
  ticket that is already started, and every external dependency is ticked **External
  Resolved**.

## Modified Flow

- Anchor: after Flow step 4 (_Click OK on the confirmation dialog_), when a dependency
  above is not met, an error dialog names the blockers and the ticket stays **On
  Progress**. Click **OK** to close the dialog, satisfy the blockers and confirm the
  ticket again. The same dependencies are checked again when the last approval completes
  the ticket.

## Additional Post-Condition

- When the dependencies are met, the status changes to **Waiting for Approval** as
  usual.
