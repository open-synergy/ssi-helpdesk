# Edit Helpdesk Ticket

> **Module:** `ssi_helpdesk_elearning`
>
> **Extends:** `ssi_helpdesk` — model `helpdesk_ticket`, aksi `02-edit`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_elearning` is installed — without it the documentation line
  has no **Course** and **Content** fields.
- **Data:** At least one e-learning course with content exists, if the line should link
  to course content.

## Additional Fields

When this module is installed, each line of the **Resolution Documentation(s)** tab
gains two optional fields in the line form:

- **Course**: The e-learning course that documents the resolution. Changing the course
  clears **Content**.
- **Content**: The content of the selected course. The list is limited to the content of
  the selected **Course**. Selecting a content fills **Documentation** with the content
  name and **URL** with the content website address, replacing what was there before.
  Clearing the content clears **URL**.

Selecting a **Type** still fills **Documentation** with the type name, as in the base
module. When both **Type** and **Content** are set, the content name is used.

## Modified Flow

- Anchor: after Flow step 4 of the base instruction (change the required fields), open
  the **Resolution Documentation(s)** tab and click **Add a line**.
- The line form shows the **Course** and **Content** fields below **Type**.
- Select a **Course**, then a **Content**; **Documentation** and **URL** are filled
  automatically. Click **Save** on the line, then continue with Flow step 5 of the base
  instruction.
