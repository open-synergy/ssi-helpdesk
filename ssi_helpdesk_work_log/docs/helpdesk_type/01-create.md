# Create Helpdesk Type

> **Module:** `ssi_helpdesk_work_log`\
> **Extends:** ssi_helpdesk — model `helpdesk_type`, action `01-create`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_work_log` is installed.

## Additional Fields

The create form gains a **Work Log** tab. Fill in the following fields when the tickets
of this type need a work estimate or work log accounting:

- **Work Estimation**: Enter the estimated working time, in hours and minutes, that a
  ticket of this type is expected to take. Optional. Tickets of this type copy this
  value into their own **Work Estimation** when the type is selected.
- **Work Log Analytic Account**: Select the analytic accounts that may be used when work
  is logged against tickets of this type. Optional.
- **Work Log Analytic Group**: Select the analytic groups that may be used when work is
  logged against tickets of this type. Optional.
