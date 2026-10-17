# Create Helpdesk Priority

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_priority`
>
> **Menu:** Helpdesk > Configuration > Ticket > Priorities
>
> **Actor:** user in group _Helpdesk Priority_
>
> **State:** `—` → `draft`

## Pre-Condition

- **Access:** User is in group _Helpdesk Priority_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Priorities** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: Enter a descriptive name for the priority.
   - **Code**: Enter **/** if no unique identifier is needed, or type a code manually.
     The **Generate Code** button on the form header assigns a code from a sequence
     template; no sequence template is shipped for this model, so type the code
     manually.
   - **Sequence**: Enter the priority order. A lower sequence means a higher priority
     and is listed first. Defaults to 10.
4. Click **Save**.

## Post-Condition

- A new record is created and active.
