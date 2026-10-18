# Create Helpdesk Resolution Documentation Type

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_resolution_documentation_type`\
> **Menu:** Helpdesk > Configuration > Ticket > Resolution Documentation Types\
> **Actor:** user in group `Helpdesk - Configurator / Helpdesk Resolution Documentation Type`\
> **Inline Actions:** `action_generate_code` (Generate Code), `action_reset_code` (Reset
> code)

## Pre-Condition

- **Config:** A `sequence.template` for this model must be configured before using the
  **Generate Code** button (see step 6). Not required when **Code** is entered manually.
- **Access:** User is in group
  `Helpdesk - Configurator / Helpdesk Resolution Documentation Type`.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Resolution Documentation Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the type.
   - **Code** _(required)_: Enter a unique code for this type, or fill with **/** and
     use the **Generate Code** button later (see step 6) to assign one automatically.
4. Optionally set the requirements of the type:
   - **Required Evidence Kind**: choose the kind of evidence a line of this type must
     use. Leave empty to accept any kind.
   - **Requires Customer Confirmation**: check it when the line must be proven by a
     message sent by the customer.
   - **Third Party**: check it when a third party is involved. It is informative only.
   - **Requires Root Cause**: check it when a root cause must be filled.
5. Optionally, on the **Note** tab, enter a free-text note.
6. If **Code** was left as **/**, click the **Generate Code** button in the header to
   automatically assign a code from the configured `sequence.template`. Skip this step
   if an explicit code was entered manually — **Generate Code** only changes records
   whose **Code** is still **/**. To undo a previously generated code later, select the
   record in the **Resolution Documentation Types** list, click **Reset code** in the
   list toolbar, then click **OK** to confirm — this clears **Code** back to **/** so it
   can be regenerated.
7. Click **Save**.

## Post-Condition

- A new Helpdesk Resolution Documentation Type record is created, active, and shown in
  the **Resolution Documentation Types** list.
- It is available for selection as **Type** on a ticket resolution documentation line.
- The requirements entered are saved on the type and decide when a line of this type is
  **Done** (see the ticket edit instruction).
- If **Generate Code** was used, **Code** shows the value assigned by the sequence
  template; otherwise it keeps the manually entered value.
