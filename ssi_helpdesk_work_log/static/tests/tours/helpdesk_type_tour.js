/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk_work_log.helpdesk_type_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/helpdesk_type/01-create.md
    // Delta tour: the navigation comes from the base work instruction;
    // the only assertion is that the Work Log tab added by this module is
    // displayed on the create form.
    tour.register(
        "ssi_helpdesk_work_log_helpdesk_type_create",
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
                content: "Work Estimation is displayed",
                trigger: ".o_form_label:contains(Work Estimation)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Work Log Analytic Account is displayed",
                trigger: ".o_form_label:contains(Work Log Analytic Account)",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Work Log Analytic Group is displayed",
                trigger: ".o_form_label:contains(Work Log Analytic Group)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
