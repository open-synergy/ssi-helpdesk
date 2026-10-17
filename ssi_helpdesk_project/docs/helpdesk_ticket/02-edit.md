# Edit Helpdesk Ticket

> **Module:** `ssi_helpdesk_project`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, aksi `02-edit`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_project` is installed.

## Additional Fields

When this module is installed, the ticket form gains a **Tasks** tab, placed after the
first tab. The fields the user can change on it:

- **Project**: The project the tasks of this ticket are created in. Optional, but the
  **Create** button on the tab creates nothing until it is filled in.
- **Need Task**: Ticked automatically from the ticket type when the type is selected. It
  can be changed manually.

The other fields on the tab (task counters, **Task Block**, **Task Done** and the
timebox dates) are computed and read-only.

## Related Views

- **Open** button on the **Tasks** tab (`action_open_task`): opens the **Tasks** list
  (project tasks) filtered to the tasks linked to the ticket. It only navigates; it
  writes nothing and has no step of its own.
