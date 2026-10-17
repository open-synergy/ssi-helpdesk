# Edit Helpdesk Type

> **Module:** `ssi_helpdesk_data_requirement`\
> **Extends:** ssi_helpdesk — model `helpdesk_type`, aksi `02-edit`

## Additional Fields

When this module is installed, the helpdesk type form gains a **Data Requirements** tab.
Each line of the tab has these fields:

- **Data Requirement Type** _(required)_: the kind of data requirement that tickets of
  this type must fulfil.
- **Title**: an optional label for the line.

## Modified Flow

- Anchor: after Flow step 3 (_Change the required fields_), open the **Data
  Requirements** tab.
- Click **Add a line** to insert a new line at the top of the list, then fill in **Data
  Requirement Type** and, optionally, **Title**.
- Click an existing line to change it, or use the line's delete icon to remove it.
- Continue with Flow step 4 (_Click **Save**_) to store the lines together with the
  type.

## Additional Post-Condition

- The saved lines are the data requirements that tickets of this type are asked to
  fulfil.
