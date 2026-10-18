# Edit Helpdesk Resolution Documentation Type

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_resolution_documentation_type`\
> **Menu:** Helpdesk > Configuration > Ticket > Resolution Documentation Types\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Resolution Documentation Type`\
> **Requires:** `01-create`\
> **Inline Actions:** `action_generate_code` (Generate Code), `action_reset_code` (Reset
> code)

## Pre-Condition

- **Access:** User is in group
  `Helpdesk - Configurator / Helpdesk Resolution Documentation Type`.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Resolution Documentation Types** menu.
2. Find and open the record to edit.
3. Click the **Edit** button. **(14.0 only — the form opens directly editable on
   16.0+)**
4. Change the **Name**, **Code**, **Note**, or the requirements (**Required Evidence
   Kind**, **Requires Customer Confirmation**, **Third Party**, **Requires Root Cause**)
   as needed.
5. If **Code** needs to be reassigned, first select the record in the **Resolution
   Documentation Types** list and click **Reset code** in the list toolbar, then click
   **OK** to confirm — this clears **Code** back to **/**. Reopen the record, click
   **Edit**, then click the **Generate Code** button in the header to assign a new code
   from the configured `sequence.template`. Both steps are optional; skip them to keep
   the current code unchanged.
6. Click **Save**.

## Post-Condition

- The record is updated with the new values.
