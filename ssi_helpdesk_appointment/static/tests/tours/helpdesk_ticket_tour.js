/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk_appointment.helpdesk_ticket_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Flow step 2 of the base IK docs/helpdesk_ticket/02-edit.md in
    // ssi_helpdesk: "Find and open the record to edit." Tickets is the
    // first child of the Helpdesk app, so it is also the app's landing
    // action: clicking it reloads an IDENTICAL action. A stale-marker gate
    // is used instead of a presence gate (odoo-development-ui-test,
    // patterns-advanced-gotchas.md section T).
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

    // IK: docs/helpdesk_ticket/02-edit.md
    tour.register(
        "ssi_helpdesk_appointment_helpdesk_ticket_edit",
        {
            test: true,
            url: "/web",
        },
        [].concat(openTicketsList(), [
            // Base Flow 2 -- Find and open the record to edit.
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(Tour HD AP Edit Ticket) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },

            // Base Flow 3 -- Click the Edit button (14.0 only).
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

            // Base Flow 4 + delta -- Open the Appointments tab and add the
            // appointment request.
            {
                content: "Open the Appointments tab",
                trigger: ".o_notebook .nav-link:contains(Appointments)",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Click Add a line on Appointment Requests",
                trigger:
                    ".o_field_many2many[name='appointment_schedule_ids'] .o_field_x2many_list_row_add a",
            },
            {
                content: "Select the appointment request in the dialog",
                trigger:
                    ".o_list_view .o_data_row:contains(Tour HD AP Contact) .o_list_record_selector input",
                in_modal: true,
                run: "click",
            },
            {
                content: "Confirm the selection",
                trigger: ".modal-footer .o_select_button:enabled",
                in_modal: true,
            },
            {
                content: "The request is listed on the tab",
                trigger:
                    ".o_field_many2many[name='appointment_schedule_ids'] .o_data_row:contains(Tour HD AP Contact)",
                extra_trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },

            // Base Flow 5 -- Click Save.
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

            // Additional Post-Condition -- the request stays listed on the
            // Appointments tab after saving.
            {
                content: "Open the Appointments tab again",
                trigger: ".o_notebook .nav-link:contains(Appointments)",
                extra_trigger: ".o_form_view.o_form_readonly",
            },
            {
                content: "The saved request is listed on the tab",
                trigger:
                    ".o_form_readonly .o_field_many2many[name='appointment_schedule_ids'] .o_data_row:contains(Tour HD AP Contact)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ])
    );
});
