# Create Helpdesk Type

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_type`
>
> **Menu:** Helpdesk > Configuration > Ticket > Types
>
> **Actor:** user in group _Helpdesk Type_
>
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** At least one `helpdesk_type_category` record exists.
- **Access:** User is in group _Helpdesk Type_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: Enter a descriptive name for the type.
   - **Code**: Enter **/** if no unique identifier is needed, or type a code manually.
     The **Generate Code** button on the form header assigns a code from a sequence
     template; no sequence template is shipped for this model, so type the code
     manually.
   - **Category**: Select the helpdesk type category this type belongs to.
   - **Duration**: Optionally select the duration used for tickets of this type.
   - **Default Priority**: Optionally select the priority given to tickets of this type.
     Leave empty to keep the ticket priority unchanged.
4. Click **Save**.

## Post-Condition

- A new record is created and active.
