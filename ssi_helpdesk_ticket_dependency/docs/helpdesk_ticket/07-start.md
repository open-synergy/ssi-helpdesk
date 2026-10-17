# Start Helpdesk Ticket

> **Module:** `ssi_helpdesk_ticket_dependency`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, aksi `07-start`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_ticket_dependency` is installed.
- **Record:** Every _Finish to Start_ dependency of the ticket has a blocker ticket that
  is **Done**, **Cancelled** or **Terminated**, and every _Start to Start_ dependency
  has a blocker ticket that is already started (**On Progress** or later).

## Modified Validation

- Start will fail if a _Finish to Start_ dependency has a blocker ticket that is not
  **Done**, **Cancelled** or **Terminated**, or if a _Start to Start_ dependency has a
  blocker ticket that has not started yet (not **On Progress** or later). The error
  message names the blocker tickets and their dependency types, and the ticket stays
  **Ready to Start**.

## Additional Post-Condition

- When the dependencies are met, the status changes to **On Progress** as usual.
