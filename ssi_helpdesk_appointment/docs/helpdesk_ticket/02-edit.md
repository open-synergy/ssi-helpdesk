# Edit Helpdesk Ticket

> **Module:** `ssi_helpdesk_appointment`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, aksi `02-edit`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_appointment` is installed.
- **Record:** An appointment request exists that is not yet linked to the ticket.

## Additional Fields

When this module is installed, the ticket form gains an **Appointments** tab. Open the
tab in step 4 of the base Flow:

- **Appointment Requests**: Click **Add a line**, then select the appointment requests
  that belong to this ticket and confirm the selection. Remove a request with the delete
  icon on its row. The field is optional.
- **Appointment Request Status** _(read-only)_: Shows **Not Needed** while no
  appointment request is linked. It shows **In Progress** while at least one linked
  request has no appointment or its appointment is not **Done**, and **Done** once every
  linked request has a **Done** appointment. It is updated automatically.

## Additional Post-Condition

- The selected appointment requests are listed on the **Appointments** tab.
- **Appointment Request Status** is recalculated from the linked requests.
