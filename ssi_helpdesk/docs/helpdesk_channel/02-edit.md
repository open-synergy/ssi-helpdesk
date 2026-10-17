# Edit Helpdesk Channel

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_channel`
>
> **Menu:** Helpdesk ‣ Configuration ‣ Communication ‣ Channels
>
> **Actor:** user in group `Helpdesk Channel`
>
> **Requires:** `01-create`
>
> **Inline Actions:** `action_generate_code` (Generate Code), `action_reset_code` (Reset
> code)

## Pre-Condition

- **Record:** A Helpdesk Channel record exists.
- **Access:** User is in group `Helpdesk Channel`.

## Flow

1. Open the **Helpdesk ‣ Configuration ‣ Communication ‣ Channels** menu.
2. Find and open the record to edit.
3. Change the required fields (Name, Code).
4. Click **Generate Code** in the header to assign a code from the configured
   `sequence.template`, if the Code field is still **/**. This requires an active
   `sequence.template` for `helpdesk_channel` — without one, the action fails with an
   error. You may also type the code manually instead.
5. Click **Save**.
6. To make the record eligible for **Generate Code** again, go back to the **Channels**
   list, select the record's checkbox, click **Reset code** in the header, then click
   **OK** to confirm. This resets the Code field back to **/**.

## Post-Condition

- The record is updated with the new values.
