# Edit Task

> **Module:** `ssi_helpdesk_project`\
> **Extends:** ssi_project — model `project.task`, aksi `02-edit`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_project` is installed.

## Related Views

- **Tickets** tab: lists the helpdesk tickets linked to the task. The **Open** button on
  the tab (`action_open_ticket`) opens the **Helpdesk Tickets** list filtered to those
  tickets. It only navigates; it writes nothing and has no step of its own.
- **Ticket Deadline** (form field and optional list column): read-only. It shows the
  earliest deadline among the linked tickets that are not done, cancelled or rejected.
