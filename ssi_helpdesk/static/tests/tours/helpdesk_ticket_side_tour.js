/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk.helpdesk_ticket_side_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Navigation block shared by every tour below -- Flow step 1 of every IK:
    // "Open the Helpdesk > Tickets menu." Tickets is the first child of the
    // Helpdesk app, so it is also the app's landing action and clicking it
    // reloads an IDENTICAL action; a stale-marker gate is used instead of a
    // presence gate (odoo-development-ui-test, patterns-advanced-gotchas.md
    // section T).
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

    // Open the fixture record whose Title is shown in the list.
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

    // Click a statusbar button, then OK on its confirmation dialog.
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

    // Open the Communications tab (Flow step 3 of the two communication IKs)
    // and wait for its buttons.
    function openCommunicationsTab() {
        return [
            {
                content: "Open the Communications tab",
                trigger: ".o_notebook .nav-link:contains(Communications)",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Communications tab is displayed",
                trigger:
                    ".o_notebook .tab-pane.active button[name='action_open_communication']",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ];
    }

    // IK: docs/helpdesk_ticket/10-cancel.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_cancel",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to cancel.
            openTicket("Tour HD Cancel Ticket"),
            [
                // Flow 3 -- Click the Cancel button. Its name is the numeric
                // id of the wizard action, so it is matched by label.
                {
                    content: "Click the Cancel button",
                    trigger: ".o_statusbar_buttons button:enabled:contains('Cancel')",
                    extra_trigger: ".o_form_view",
                },
                {
                    content: "Wizard is displayed",
                    trigger: ".modal-title:contains(Select Cancel Reason)",
                    in_modal: false,
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },

                // Flow 4 -- Select the Reason (radio widget).
                {
                    content: "Select the cancellation reason",
                    trigger:
                        ".o_field_widget[name='cancel_reason_id'] .o_radio_item:contains(Tour HD Reason) input",
                },

                // Flow 5 -- Click Confirm on the wizard.
                {
                    content: "Confirm the wizard",
                    trigger: ".modal-footer button[name='action_confirm']",
                },

                // Flow 6 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                },
            ],
            // Post-Condition -- Status is Cancelled and the reason is shown.
            assertStatus("cancel", "Cancelled"),
            [
                {
                    content: "Cancellation reason is shown",
                    trigger:
                        ".o_form_view .o_field_widget[name='cancel_reason_id']:contains(Tour HD Reason)",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },
            ]
        )
    );

    // IK: docs/helpdesk_ticket/12-restart.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_restart",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            [
                // Flow 2 -- The default filters hide cancelled tickets: open
                // the Filters menu and select Cancel.
                {
                    content: "Open the Filters menu",
                    trigger: ".o_search_options .o_filter_menu button",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Select the Cancel filter",
                    trigger: ".o_filter_menu .dropdown-item:contains(Cancel)",
                    run: function () {
                        var $item = $(".o_filter_menu .dropdown-item").filter(
                            function () {
                                return $(this).text().trim() === "Cancel";
                            }
                        );
                        $item[0].click();
                    },
                },
                {
                    // The row cannot be listed before the filter is applied.
                    content: "Cancelled ticket is listed",
                    trigger: ".o_data_row:contains(Tour HD Restart Ticket)",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },
            ],
            // Flow 3 -- Open the record to restart.
            openTicket("Tour HD Restart Ticket"),
            // Flow 4-5 -- Click Restart, then OK on the dialog.
            clickButtonAndConfirm("action_restart", "Restart"),
            // Post-Condition -- Status changes to Draft.
            assertStatus("draft", "Draft")
        )
    );

    // IK: docs/helpdesk_ticket/15-split.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_split",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to split.
            openTicket("Tour HD Split Ticket"),
            [
                // Flow 3 -- Open the Duplicate & Split tab.
                {
                    content: "Open the Duplicate & Split tab",
                    trigger: ".o_notebook .nav-link:contains(Split)",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click the Split Ticket button (type="action", so
                // matched by label).
                {
                    content: "Click the Split Ticket button",
                    trigger:
                        ".o_notebook .tab-pane.active button:contains('Split Ticket')",
                },
                {
                    content: "Wizard is displayed",
                    trigger: ".modal-title:contains(Split Ticket)",
                    in_modal: false,
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },

                // Flow 5 -- Fill in the wizard. Category first: changing it
                // clears Type.
                {
                    content: "Fill in the Title",
                    trigger: ".o_field_widget[name='title']",
                    run: "text Tour HD Split Child",
                },
                {
                    content: "Select the Category",
                    trigger: ".o_field_many2one[name='category_id'] input",
                    run: "text Tour HD Category",
                },
                {
                    content: "Pick the Category from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour HD Category)",
                    in_modal: false,
                },
                {
                    content: "Select the Type",
                    trigger: ".o_field_many2one[name='type_id'] input",
                    run: "text Tour HD Type",
                },
                {
                    content: "Pick the Type from the dropdown",
                    trigger: ".ui-autocomplete .ui-menu-item a:contains(Tour HD Type)",
                    in_modal: false,
                },

                // Flow 6 -- Click Confirm on the wizard.
                {
                    content: "Confirm the wizard",
                    trigger: ".modal-footer button[name='action_confirm']",
                },

                // Flow 7 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                },

                // Post-Condition -- The new ticket form is displayed with the
                // title entered in the wizard.
                {
                    content: "The new ticket is displayed",
                    trigger:
                        ".o_form_view .o_field_widget[name='title']:contains(Tour HD Split Child)",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },
            ]
        )
    );

    // IK: docs/helpdesk_ticket/16-create-finishing-communication.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_create_finishing_communication",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to finish.
            openTicket("Tour HD Finishing Ticket"),
            // Flow 3 -- Open the Communications tab.
            openCommunicationsTab(),
            [
                // Flow 4 -- Click the Finishing button.
                {
                    content: "Click the Finishing button",
                    trigger:
                        ".o_notebook .tab-pane.active button[name='action_create_finishing_communication']",
                },

                // Post-Condition -- The new communication form is displayed
                // in Draft status, titled like the ticket.
                {
                    content: "The new communication is displayed",
                    trigger:
                        ".o_form_view .o_field_widget[name='title']:contains(Tour HD Finishing Ticket)",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },
            ],
            assertStatus("draft", "Draft")
        )
    );

    // IK: docs/helpdesk_ticket/17-create-updating-communication.md
    tour.register(
        "ssi_helpdesk_helpdesk_ticket_create_updating_communication",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            // Flow 2 -- Open the record to report on.
            openTicket("Tour HD Updating Ticket"),
            // Flow 3 -- Open the Communications tab.
            openCommunicationsTab(),
            [
                // Flow 4 -- Click the Updating button.
                {
                    content: "Click the Updating button",
                    trigger:
                        ".o_notebook .tab-pane.active button[name='action_create_updating_communication']",
                },

                // Post-Condition -- The new communication form is displayed
                // in Draft status with the status update title.
                {
                    content: "The new communication is displayed",
                    trigger:
                        ".o_form_view .o_field_widget[name='title']:contains(Ticket status update)",
                    run: function () {
                        // Assertion only; do not trigger the default click.
                    },
                },
            ],
            assertStatus("draft", "Draft")
        )
    );
});
