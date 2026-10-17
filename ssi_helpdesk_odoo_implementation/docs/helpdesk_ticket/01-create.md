# Create Helpdesk Ticket

> **Module:** `ssi_helpdesk_odoo_implementation`\
> **Extends:** ssi_helpdesk — model `helpdesk_ticket`, action `01-create`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_odoo_implementation` is installed.
- **Data:** To link the ticket to an implementation, an Odoo implementation owned by the
  selected **Commercial Contact** exists.

## Additional Fields

- **Odoo Implementation** _(header)_: Select the Odoo implementation the ticket is
  about. Only implementations of the selected **Commercial Contact** are offered.
- **Odoo Version** _(header)_: Read-only. Shows the version of the selected Odoo
  implementation.
- **Odoo Feature** _(header)_: Select the related Odoo features. Several features can be
  selected.
- **Related Use Case Specifications** _(tab **Odoo Implementation**)_: Select the use
  case specifications that relate to the ticket.
- **Change Request > Required** _(tab **Odoo Implementation**)_: Switch on if the ticket
  needs a change request. Then select the change requests in the list below it.
  **State** is read-only and follows the selected change requests.
- **Configuration Change Record > Required** _(tab **Odoo Implementation**)_: Switch on
  if the ticket needs a configuration change record. Then select the records in the list
  below it. **State** is read-only and follows the selected records.
- **Issue > State** _(tab **Odoo Implementation**)_: Read-only. Follows the selected
  Odoo feature issues in the list below it.

## Modified Flow

- Anchor: after Flow step 4 (optional header fields), optionally fill in **Odoo
  Implementation** and **Odoo Feature** in the header.
- Anchor: after Flow step 5 (**Description** tab), optionally open the **Odoo
  Implementation** tab and fill in the fields listed above.
