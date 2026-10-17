/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk.helpdesk_ticket_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block, reused verbatim by every tour below -- Flow
    // step 1 of every IK in docs/helpdesk_ticket/: "Open the Helpdesk >
    // Tickets menu." Tickets is the first child of the Helpdesk app, so it
    // is also the app's landing action: clicking it reloads an IDENTICAL
    // action. A stale-marker gate is used instead of a presence gate
    // (odoo-development-ui-test, patterns-advanced-gotchas.md §T).
    function openTicketsList() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Helpdesk app",
                trigger: '.o_app[data-menu-xmlid="ssi_helpdesk.menu_root_helpdesk"]',
            },
            {
                content: "Open the Tickets menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_ticket_menu"]',
                run: function (actions) {
                    // Instrumentation only: dies together with the old
                    // controller.
                    $(".o_control_panel").addClass("oe_tour_stale");
                    actions.click();
                },
            },
            {
                content: "Tickets list is displayed",
                trigger:
                    ".o_control_panel:not(.oe_tour_stale) .breadcrumb-item.active:contains(Helpdesk Tickets)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ];
    }

    // Open the fixture record whose Title is shown in the list (the Title
    // column is always visible; the document number is "*<id>" in Draft).
    function openTicket(title) {
        return [
            {
                content: "Open the record",
                trigger: ".o_data_row:contains(" + title + ") .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ];
    }

    // Click a statusbar button, then OK on the confirmation dialog
    // (confirm="..." on the button -- form view only).
    function clickButtonAndConfirm(name, label) {
        return [
            {
                content: "Click the " + label + " button",
                trigger: ".o_statusbar_buttons button[name='" + name + "']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
        ];
    }

    // Post-Condition assertion on the statusbar.
    function assertStatus(value, label) {
        return [
            {
                content: "Status is " + label,
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='" +
                    value +
                    "'].btn-primary",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ];
    }

    // IK: docs/helpdesk_ticket/01-create.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            [
                // Flow 2 -- Click the New button.
                {
                    content: "Click Create",
                    trigger: ".o_list_button_add",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Form is open in edit mode",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },

                // Flow 3 -- Fill in the required fields in the header. Select
                // the Commercial Contact first: it drives the domain of Contact
                // and clears it on change. Date defaults to today and is left
                // as-is.
                {
                    content: "Select the Commercial Contact",
                    trigger: ".o_field_many2one[name='commercial_partner_id'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Tour HD Create Company",
                },
                {
                    content: "Pick the Commercial Contact from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour HD Create Company)",
                    in_modal: false,
                },
                {
                    content: "Select the Contact",
                    trigger: ".o_field_many2one[name='partner_id'] input",
                    run: "text Tour HD Create Contact",
                },
                {
                    content: "Pick the Contact from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour HD Create Contact)",
                    in_modal: false,
                },
                {
                    content: "Fill in the Title",
                    trigger: ".o_field_widget[name='title']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Tour HD Create Ticket",
                },
                {
                    // The required Priority is pre-filled (IK 01-create
                    // step 4); the tour only checks that it is shown.
                    content: "Priority field is shown",
                    trigger: ".o_field_many2one[name='priority_id']",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Flow 6 -- Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },
            ],
            assertStatus("draft", "Draft")
        )
    );

    // IK: docs/helpdesk_ticket/02-edit.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_edit",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Find and open the record to edit.
            openTicket("Tour HD Edit Ticket"),
            [
                // Flow 3 -- Click the Edit button (14.0 only).
                {
                    content: "Click the Edit button",
                    trigger: ".o_form_button_edit",
                },
                {
                    content: "Form is now editable",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },

                // Flow 4 -- Change the Title.
                {
                    content: "Change the Title",
                    trigger: ".o_field_widget[name='title']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Tour HD Edit Ticket Changed",
                },

                // Flow 5 -- Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },

                // Post-Condition -- The record is updated with the new
                // values. Go back to the list and reopen the record so the
                // title is read from a genuine text node.
                {
                    content: "Go back to the list",
                    trigger:
                        ".breadcrumb-item:not(.active):contains('Helpdesk Tickets')",
                },
                {
                    content: "Reopen the record",
                    trigger:
                        ".o_data_row:contains(Tour HD Edit Ticket Changed) .o_data_cell:first",
                },
                {
                    content: "Title shows the new value",
                    trigger:
                        ".o_form_readonly .o_field_widget[name='title']:contains('Tour HD Edit Ticket Changed')",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },
            ]
        )
    );

    // IK: docs/helpdesk_ticket/03-delete.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_delete",
        {
            test: true,
            url: "/web",
        },
        [].concat(openTicketsList(), [
            // Flow 2 -- Select the record to delete (check the checkbox).
            {
                content: "Select the record to delete",
                trigger:
                    ".o_data_row:contains(Tour HD Delete Ticket) .o_list_record_selector input",
                extra_trigger: ".o_list_view",
                run: "click",
            },

            // Flow 3 -- Click Action > Delete.
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
                // 14.0: the Action dropdown is an Owl component that does
                // not always open on a synthetic click
                // (odoo-development-ui-test, patterns.md §I).
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Click Delete",
                // Match the label EXACTLY -- :contains(Delete) as a
                // substring could match another item.
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $delete = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Delete";
                        }
                    );
                    $delete[0].click();
                },
            },

            // Flow 4 -- Click OK on the confirmation dialog.
            {
                content: "Confirm deletion",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // Post-Condition -- The selected record is removed.
            {
                content: "Record no longer appears in the list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(Tour HD Delete Ticket)))",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ])
    );

    // IK: docs/helpdesk_ticket/08-ready.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_ready",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to stage.
            openTicket("Tour HD Ready Ticket"),
            // Flow 3-4 -- Click Stage, then OK on the dialog.
            clickButtonAndConfirm("action_ready", "Stage"),
            // Post-Condition -- Status changes to Ready to Start.
            assertStatus("ready", "Ready to Start")
        )
    );

    // IK: docs/helpdesk_ticket/07-start.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_start",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to start.
            openTicket("Tour HD Start Ticket"),
            // Flow 3-4 -- Click Start, then OK on the dialog.
            clickButtonAndConfirm("action_open", "Start"),
            // Post-Condition -- Status changes to On Progress.
            assertStatus("open", "On Progress")
        )
    );

    // IK: docs/helpdesk_ticket/04-confirm.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_confirm",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to confirm.
            openTicket("Tour HD Confirm Ticket"),
            // Flow 3-4 -- Click Confirm, then OK on the dialog.
            clickButtonAndConfirm("action_confirm", "Confirm"),
            // Post-Condition -- Status changes to Waiting for Approval.
            assertStatus("confirm", "Waiting for Approval")
        )
    );

    // IK: docs/helpdesk_ticket/05-approve.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_approve",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to approve.
            openTicket("Tour HD Approve Ticket"),
            // Flow 3-4 -- Click Approve, then OK on the dialog.
            clickButtonAndConfirm("action_approve_approval", "Approve"),
            // Post-Condition (all approval levels fulfilled) -- status
            // changes to Done.
            assertStatus("done", "Done")
        )
    );

    // IK: docs/helpdesk_ticket/06-reject.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_reject",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to reject.
            openTicket("Tour HD Reject Ticket"),
            // Flow 3-4 -- Click Reject, then OK on the dialog.
            clickButtonAndConfirm("action_reject_approval", "Reject"),
            // Post-Condition -- Status changes to Rejected.
            assertStatus("reject", "Rejected")
        )
    );
});
