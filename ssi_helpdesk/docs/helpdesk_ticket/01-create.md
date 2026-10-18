# Create Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** A commercial contact (a company without a parent) exists.
- **Data:** A contact (a person whose parent is that company) exists.
- **Access:** User is in group _Helpdesk Ticket / User_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields in the header:
   - **Commercial Contact** _(required)_: Select the customer company that raises the
     ticket. Only companies without a parent are offered.
   - **Contact** _(required)_: Select the person who raises the ticket. Available
     options are the contacts of the selected **Commercial Contact**. Changing the
     **Commercial Contact** clears this field.
   - **Title** _(required)_: Enter a short title for the ticket. Automatically filled if
     a **Type** is selected and its **Category** is configured to build the title
     automatically. Change if needed.
   - **Date** _(required)_: Automatically filled with today's date. Change if needed.
4. Optionally fill in the other header fields:
   - **Responsible**: Automatically filled with the current user. Change if needed.
   - **Contact Group**: Select the contact groups of the **Commercial Contact** that
     should be kept informed. Reset when **Contact** changes.
   - **CC To**: Select additional contacts that should receive updates. Reset when
     **Contact** or **Contact Group** changes.
   - **Category**: Select the ticket category.
   - **Type**: Select the ticket type. Available options are based on **Category**.
   - **Tags**: Select one or more tags. Available options are the tags of the categories
     that are enabled for all documents or linked to the ticket model.
     Selecting a **Type** resets the **Title** unless the **Category** builds it
     automatically, so fill in the **Title** after selecting the **Type**. It also adds
     the required resolution documentations of the **Type** to the **Resolution
     Documentation(s)** tab, without removing lines you added yourself and without
     repeating a documentation type already listed.
   - **Priority** _(required)_: Automatically filled with **Medium**, or with the
     **Default Priority** of the selected **Type** when it has one. Change if needed.
   - **Duration**: Automatically filled from **Type**. Change if needed.
   - **Deadline**: Automatically filled from **Duration** and **Date**. Change if
     needed.
   - **Update Progress**: Keep checked if the customer expects progress updates.
5. Optionally, on the **Description** tab, describe the problem.
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- A document number is generated automatically when the record is created.
- When a **Type** with required documentations was selected, they are listed on the
  **Resolution Documentation(s)** tab.
