# Create Helpdesk Contact Group

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_contact_group`
>
> **Menu:** Helpdesk ‣ Configuration ‣ Ticket ‣ Contact Groups
>
> **Actor:** user in group `Helpdesk Contact Group`
>
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Data:** At least one commercial contact (a partner without a parent company) and one
  contact partner exist, to be chosen in the **Commercial Contact** and **Contacts**
  fields.
- **Access:** User is in group `Helpdesk Contact Group`.

## Flow

1. Open the **Helpdesk ‣ Configuration ‣ Ticket ‣ Contact Groups** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the contact group.
   - **Code** _(required)_: Enter a unique code identifying this contact group, or enter
     **/** to assign it later using **Generate Code**.
   - **Commercial Contact** _(required)_: Select the commercial contact (a partner
     without a parent company) that the group belongs to.
   - **Contacts** _(required)_: Select one or more contacts that belong to the group.
4. Click **Generate Code** in the header to automatically assign a code from the
   `sequence.template` configured for `helpdesk_contact_group`. This requires an active
   `sequence.template` for this model — without one, the action fails with an error. You
   may also leave the Code field as **/** or type a code manually instead.
5. Click **Save**.

## Post-Condition

- A new Helpdesk Contact Group record is created and active.
- The new Helpdesk Contact Group becomes selectable on Helpdesk Ticket records.
