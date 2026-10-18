# Edit Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Access:** User is in group _Helpdesk Ticket / User_.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Find and open the record to edit.
3. Click the **Edit** button. **(14.0 only — the form opens directly editable on
   16.0+)**
4. Change the required fields (for example **Title**). Optionally add or remove
   **Tags**.
5. To prove a resolution documentation, open the **Resolution Documentation(s)** tab and
   click **Add a line**.
6. Fill **Documentation**.
7. Choose the **Evidence Kind**: **Message**, **Odoo Record**, **Decision**, **URL** or
   **Code**.
8. Fill the evidence of that kind:
   - **Message**: select the **Message**, taken from the emails and comments of the
     ticket and of its communications. **Confirmed By** and **Evidence Channel** are
     read from the message, and **Evidence Date** follows the message date.
   - **Odoo Record**: select the **Odoo Record**.
   - **Decision**: write the **Decision**.
   - **URL** or **Code**: fill the **URL** (for example the link of a pull request).
9. Click **Save & Close** on the line.
10. To mark a documentation as not applicable, click **Add a line** again, fill
    **Documentation**, tick **Not Applicable** and fill **Not Applicable Reason**
    (required), then click **Save & Close** on the line.
11. Click **Save**.

## Post-Condition

- The record is updated with the new values.
- A line is **Done** when the evidence of its kind is filled. A line without an
  **Evidence Kind** and with a **URL** is also **Done**.
- When the **Type** of the line has requirements, the line is **Done** only if they are
  met: the **Evidence Kind** equals the **Required Evidence Kind** of the type; with
  **Requires Customer Confirmation** the evidence is a **Message** whose author
  (**Confirmed By**) is not a company partner; with **Requires Root Cause** the **Root
  Cause** is filled. Otherwise the line stays **In Progress**.
- A line marked **Not Applicable** has the state **Not Applicable**, whatever its
  evidence, and a **Not Applicable Reason** is required for it.
- The **Resolution Documentation Status** of the ticket ignores the **Not Applicable**
  lines: **In Progress** while an applicable line is open, **Done** when all applicable
  lines are done, and **Not Needed** when no applicable line remains.
- Changing the evidence of a line posts a note on the ticket chatter with the old and
  the new evidence.
