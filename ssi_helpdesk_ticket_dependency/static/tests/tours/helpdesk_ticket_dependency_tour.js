/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk_ticket_dependency.helpdesk_ticket_dependency_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // Navigation shared by the three tours: Flow step 1 of the base IK,
    // "Open the Helpdesk > Tickets menu." Tickets is the landing action
    // of the app, so a stale-marker gate is used instead of a presence
    // gate.
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
                    // Assertion only.
                },
            },
        ];
    }

    // Open the fixture record by its unique Title.
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
                    // Assertion only.
                },
            },
        ];
    }

    // Click a statusbar button and confirm the dialog, then expect the
    // error dialog that names the blocker, close it and check that the
    // status did not change.
    function gateRejected(buttonName, label, blockerText, statusValue) {
        return [
            {
                content: "Click the " + label + " button",
                trigger: ".o_statusbar_buttons button[name='" + buttonName + "']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "The error dialog names the blocker",
                trigger: ".modal-body:contains(" + blockerText + ")",
                in_modal: true,
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Close the error dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
            {
                content: "Cancel the confirmation dialog that is still open",
                trigger: ".modal-footer button.btn-secondary",
                in_modal: true,
            },
            {
                content: "No dialog is left open",
                trigger: "body:not(.modal-open)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Status did not change",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='" +
                    statusValue +
                    "'].btn-primary",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/helpdesk_ticket/02-edit.md
    // Delta tour: navigation and Edit follow the base IK, then the
    // Dependencies tab is asserted. Saving is not part of this tour; dependency
    // values are a unit-test concern.
    tour.register(
        "ssi_helpdesk_ticket_dependency_helpdesk_ticket_edit",
        {
            test: true,
            url: "/web",
        },
        [].concat(openTicketsList(), openTicket("DEP75 Edit Ticket"), [
            {
                content: "Click the Edit button",
                trigger: ".o_form_button_edit",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Form is now editable",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Open the Dependencies tab",
                trigger: ".o_notebook .nav-link:contains(Dependencies)",
            },
            {
                content: "Dependencies tab is displayed",
                trigger: ".o_notebook .nav-link.active:contains(Dependencies)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Start Blocked label is displayed",
                trigger: ".o_form_label:contains(Start Blocked)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Add a line is available",
                trigger:
                    ".o_field_one2many[name='dependency_ids'] .o_field_x2many_list_row_add a",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/helpdesk_ticket/07-start.md
    tour.register(
        "ssi_helpdesk_ticket_dependency_helpdesk_ticket_start",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            openTicket("DEP75 Start Ticket"),
            gateRejected("action_open", "Start", "DEP75 Blocker Ticket", "ready")
        )
    );

    // IK: docs/helpdesk_ticket/04-confirm.md
    tour.register(
        "ssi_helpdesk_ticket_dependency_helpdesk_ticket_confirm",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openTicketsList(),
            openTicket("DEP75 Confirm Ticket"),
            gateRejected("action_confirm", "Confirm", "owner/repo#75", "open")
        )
    );
});
