# Create Helpdesk Communication

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_communication`\
> **Menu:** Helpdesk > Communications\
> **Actor:** user in group `Helpdesk Communication / User`\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** A contact (a person whose parent is a company) exists.
- **Config:** An active `sequence.template` for this model exists.
- **Access:** User is in group _Helpdesk Communication / User_.

## Flow

1. Open the **Helpdesk > Communications** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields in the header:
   - **Contact** _(required)_: Select the person who sent or receives the communication.
     Only contacts that belong to a company are offered. The **Commercial Contact** is
     filled in automatically from the selected contact.
   - **Title** _(required)_: Enter a short title for the communication.
   - **Date** _(required)_: Automatically filled with today's date. Change if needed.
4. Optionally fill in the other header fields:
   - **Responsible**: Automatically filled with the current user. Change if needed.
   - **Channel**: Select the channel through which the communication happens.
   - **# Ticket**: Select an existing ticket of the same **Commercial Contact**. Leave
     empty to create a ticket later (see `15-create-ticket`).
5. Optionally, on the **Description** tab, describe the communication.
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- A document number is assigned as soon as the record is saved.
- Communications created from an incoming email by the mail gateway follow the same
  rules: the email subject becomes the **Title**, the sender the **Contact**, and the
  email body the **Description**.
