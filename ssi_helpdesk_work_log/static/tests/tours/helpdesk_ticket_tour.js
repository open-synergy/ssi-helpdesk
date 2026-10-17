/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk_work_log.helpdesk_ticket_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/helpdesk_ticket/01-create.md
    // Delta tour: the navigation comes from the base work instruction;
    // the only assertion is that the Work Log tab added by this module is
    // displayed on the create form.
    tour.register(
        "ssi_helpdesk_work_log_helpdesk_ticket_create",
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
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Open the Work Log tab",
                trigger: ".o_notebook .nav-link:contains(Work Log)",
            },
            {
                content: "Estimation is displayed",
                trigger: ".o_form_label:contains(Estimation)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Total is displayed",
                trigger: ".o_form_label:contains(Total)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Remaining is displayed",
                trigger: ".o_form_label:contains(Remaining)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Excess is displayed",
                trigger: ".o_form_label:contains(Excess)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
