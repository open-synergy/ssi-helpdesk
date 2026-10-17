# Create Helpdesk Type

> **Module:** `ssi_helpdesk_project`\
> **Extends:** ssi_helpdesk — model `helpdesk_type`, aksi `01-create`

## Additional Pre-Condition

- **Module:** `ssi_helpdesk_project` is installed.

## Additional Fields

When this module is installed, the type form gains a **Project** tab. It is the first
tab of the form, so it is shown when the form opens. The tab holds:

- **Need Task**: Tick it when tickets of this type must be handled through project
  tasks. A ticket takes its initial **Need Task** value from its type when the type is
  selected on the ticket. Optional; unticked by default.
- **Tasks** (list under the checkbox): The task templates used by the **Create** button
  on a ticket. Optional. Click **Add a line** to add one template, then fill in:
  - **Task Summary** _(required)_: The name of the task created from this template.
  - **Task Type**: Optionally select the task type of the created task.
  - **Assigned To**: Optionally select the user the created task is assigned to.

## Modified Flow

- Anchor: after Flow base step 3 (fill in the required fields) and before step 4
  (**Save**), open the **Project** tab, tick **Need Task** and add the task templates.
  Both are optional, so the base flow also works without this step.

## Additional Post-Condition

- The type is created with its **Need Task** value and the listed task templates.
- The **Need Task** column can be shown in the types list through the optional columns
  menu.
