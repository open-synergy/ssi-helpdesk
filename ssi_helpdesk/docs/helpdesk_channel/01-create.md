# Create Helpdesk Channel

> **Module:** `ssi_helpdesk`
>
> **Model:** `helpdesk_channel`
>
> **Menu:** Helpdesk ‣ Configuration ‣ Communication ‣ Channels
>
> **Actor:** user in group `Helpdesk Channel`
>
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Access:** User is in group `Helpdesk Channel`.

## Flow

1. Open the **Helpdesk ‣ Configuration ‣ Communication ‣ Channels** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: Enter the name of the channel (e.g. "Email", "Phone").
   - **Code** _(required)_: Enter a unique code identifying this channel, or enter **/**
     to assign it later using **Generate Code**.
4. Click **Generate Code** in the header to automatically assign a code from the
   `sequence.template` configured for `helpdesk_channel`. This requires an active
   `sequence.template` for this model — without one, the action fails with an error. You
   may also leave the Code field as **/** or type a code manually instead.
5. Click **Save**.

## Post-Condition

- A new Helpdesk Channel record is created and active.
- The new Helpdesk Channel becomes selectable on Helpdesk Communication records.
