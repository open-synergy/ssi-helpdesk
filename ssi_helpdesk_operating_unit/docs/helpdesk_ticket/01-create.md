# Create Helpdesk Ticket

> **Module:** `ssi_helpdesk_operating_unit`\
> **Extends:** `ssi_helpdesk` — model `helpdesk_ticket`, aksi `01-create`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_operating_unit` is installed.
- **Access:** User is in group _Multi Operating Units_
  (`operating_unit.group_multi_operating_unit`) — without it the **Operating Unit**
  field is hidden on the form.

## Additional Fields

When this module is installed, the form gains one optional header field:

- **Operating Unit**: The operating unit the ticket belongs to. Automatically filled
  with the default operating unit of the current user. Change if needed. Users only see
  the tickets of the operating units assigned to them.

## Modified Flow

- Anchor: at Flow step 4 of the base instruction (optionally fill in the other header
  fields), the **Operating Unit** field is shown next to **Company**.

## Modified — Record Visibility

- The ticket list is filtered by operating unit (record rule). This is not a Flow step.
