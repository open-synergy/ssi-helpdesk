/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk_data_requirement.helpdesk_data_requirement_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/helpdesk_type/02-edit.md
    // Delta tour: navigation follows the base IK (open the Types menu,
    // open the record, click Edit), then the Data Requirements tab is
    // asserted and an inline line is added. Saving is not part of
    // this tour; the line values are a unit-test concern.
    tour.register(
        "ssi_helpdesk_data_requirement_helpdesk_type_edit",
        {
            test: true,
            url: "/web",
        },
        [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Helpdesk app",
                trigger: '.o_app[data-menu-xmlid="ssi_helpdesk.menu_root_helpdesk"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.menu_helpdesk_configuration"]',
            },
            {
                content: "Open the Types menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_type_menu"]',
            },
            {
                content: "Types list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Types)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Open the record",
                trigger: ".o_data_row:contains(DR75-TYPE) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
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
                content: "Open the Data Requirements tab",
                trigger: ".o_notebook .nav-link:contains(Data Requirements)",
            },
            {
                content: "Data Requirements tab is displayed",
                trigger: ".o_notebook .nav-link.active:contains(Data Requirements)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Add a line is available",
                trigger:
                    ".o_field_one2many[name='data_requirement_ids'] .o_field_x2many_list_row_add a",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_ticket/02-edit.md
    // Delta tour: navigation follows the base IK (open the Tickets
    // menu, open the record), then the Data Requirements tab and its
    // status label are asserted.
    tour.register(
        "ssi_helpdesk_data_requirement_helpdesk_ticket_edit",
        {
            test: true,
            url: "/web",
        },
        [
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
            {
                content: "Open the record",
                trigger: ".o_data_row:contains(DR75 Ticket) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Open the Data Requirements tab",
                trigger: ".o_notebook .nav-link:contains(Data Requirements)",
            },
            {
                content: "Data Requirement Status label is displayed",
                trigger: ".o_form_label:contains(Data Requirement Status)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
