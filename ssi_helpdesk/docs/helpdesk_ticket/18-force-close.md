# Force Close Helpdesk Ticket

> **Module:** `ssi_helpdesk`\
> **Model:** `helpdesk_ticket`\
> **Menu:** Helpdesk > Tickets\
> **Actor:** user in group `Helpdesk Ticket / Validator`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **On Progress** (or **Waiting for Approval**), and **Resolution
  Documentation Status** is **In Progress**: at least one resolution documentation of
  the ticket has no URL yet. The ticket has not been force closed before.
- **Config:** An active `policy.template` for this model grants `force_close_ok` for
  states `open` and `confirm` to the actor's group. The standard template grants it to
  group _Helpdesk Ticket / Validator_.
- **Access:** User is in the group granted by the `force_close_ok` policy (by default
  _Helpdesk Ticket / Validator_). Without it, the **Force Close** button is not shown.

## Flow

1. Open the **Helpdesk > Tickets** menu.
2. Open the record to force close.
3. Click the **Force Close** button.
4. In the wizard that appears, fill in the fields:
   - **Reason** _(required)_: Explain why the ticket is closed while its resolution
     documentation is still in progress.
5. Click **Confirm** on the wizard.

## Post-Condition

- **Force Close Reason** and **Force Closed By** are filled on the **Resolution
  Documentation(s)** tab, and the change is logged in the chatter.
- The **Force Close** button is no longer shown.
- The ticket can now be confirmed and finished: the open resolution documentation no
  longer blocks **Confirm** or the final approval. Force close does not bypass the split
  ticket and communication checks of `04-confirm`.
