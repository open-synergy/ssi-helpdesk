# Confirm Helpdesk Ticket

> **Module:** `ssi_helpdesk_ticket_dependency`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, aksi `04-confirm`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_ticket_dependency` is installed.
- **Record:** Every _Finish to Finish_ dependency has a blocker ticket that is **Done**,
  **Cancelled** or **Terminated**, every _Start to Finish_ dependency has a blocker
  ticket that is already started, and every external dependency is ticked **External
  Resolved**.

## Modified Validation

- Confirm will fail if a _Finish to Finish_ dependency has a blocker ticket that is not
  **Done**, **Cancelled** or **Terminated**, if a _Start to Finish_ dependency has a
  blocker ticket that has not started yet, or if an external dependency is not ticked
  **External Resolved**. The error message names the blockers, and the ticket stays **On
  Progress**. The same dependencies are checked again when the last approval completes
  the ticket.

## Additional Post-Condition

- When the dependencies are met, the status changes to **Waiting for Approval** as
  usual.
