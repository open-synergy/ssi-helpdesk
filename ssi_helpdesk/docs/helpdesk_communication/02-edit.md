# Edit Helpdesk Communication

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_communication`\
> **Menu:** Helpdesk > Communications\
> **Actor:** user in group `Helpdesk Communication / User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Access:** User is in group _Helpdesk Communication / User_.

## Flow

1. Open the **Helpdesk > Communications** menu.
2. Open the record to edit.
3. Click the **Edit** button.
4. Change the fields as needed. In **Draft** status the **Title**, **Contact**,
   **Date**, **Channel** and **Responsible** can be changed; **# Ticket**, **Tags** and
   **Description** can be changed in any status.
5. Open the **Activities** tab and, if needed, set **Waiting For** to the answer the
   company expects from the contact: **Answer**, **Confirmation** or **Information
   Only**. **Waiting For** can be changed in any status.
6. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- **Waiting For** shows the selected value. It is emptied automatically when the contact
  replies, and the ticket counts the record as waiting for an answer or a confirmation.
- Once the record has left **Draft** status, the **Title**, **Contact**, **Date**,
  **Channel** and **Responsible** become read-only.
