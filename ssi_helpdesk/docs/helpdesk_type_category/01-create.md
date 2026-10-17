# Create Helpdesk Type Category

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_type_category`
>
> **Menu:** Helpdesk > Configuration > Ticket > Categories
>
> **Actor:** user in group _Helpdesk Type Category_
>
> **State:** `—` → `draft`

## Pre-Condition

- **Access:** User is in group _Helpdesk Type Category_.

## Flow

1. Open the **Helpdesk > Configuration > Ticket > Categories** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: Enter a descriptive name for the category.
   - **Code**: Enter **/** if no unique identifier is needed, or type a code manually.
     The **Generate Code** button on the form header assigns a code from a sequence
     template; no sequence template is shipped for this model, so type the code
     manually.
   - **Auto Generate Title**: Tick to let tickets of this category generate their title
     automatically. Optional.
4. Click **Save**.

## Post-Condition

- A new record is created and active.
