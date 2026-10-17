# Create Helpdesk Ticket

> **Module:** `ssi_helpdesk_work_log`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, action `01-create`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_work_log` is installed.

## Additional Fields

The create form gains a **Work Log** tab. It is shown next to the other tabs of the
ticket and holds the following fields:

- **Estimation**: Automatically filled with the **Work Estimation** of the selected
  **Type**, and reset to zero when the **Type** is cleared. Change if needed.
- **Total**: Read-only. The total working time logged against the ticket.
- **Remaining**: Read-only. The part of the estimation that has not been logged yet.
- **Excess**: Read-only. The working time logged beyond the estimation.
- **Work Log Analytic Account**: Optional. The analytic account used when work is logged
  against the ticket.
- **Work Logs**: The work log lines recorded against the ticket.

## Additional Post-Condition

- Tickets created by the **Duplicate & Split** and **Create Ticket from Communication**
  wizards also get their **Estimation** filled from their **Type**. This does not add a
  step to the Flow.
