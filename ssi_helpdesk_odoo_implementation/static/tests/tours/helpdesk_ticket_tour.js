/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk_odoo_implementation.helpdesk_ticket_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/helpdesk_ticket/01-create.md
    // Delta-only tour: navigation comes from the base IK of ssi_helpdesk
    // (open the Tickets menu, click New); the assertions come from the
    // Additional Fields of this module's delta IK. The form is not saved.
    tour.register(
        "ssi_helpdesk_odoo_implementation_helpdesk_ticket_create",
        {
            test: true,
            url: "/web",
        },
        [
            // Base Flow 1 -- Open the Helpdesk > Tickets menu. Tickets is
            // the app's landing action, so a stale-marker gate is used
            // (odoo-development-ui-test, patterns-advanced-gotchas.md §T).
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

            // Base Flow 2 -- Click the New button.
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

            // Delta -- Additional Fields in the header.
            {
                content: "Odoo Implementation field is displayed",
                trigger: ".o_field_widget[name='odoo_implementation_id']",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Odoo Feature field is displayed",
                trigger: ".o_field_widget[name='odoo_feature_ids']",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },

            // Delta -- Additional Fields in the Odoo Implementation tab.
            {
                content: "Open the Odoo Implementation tab",
                trigger: ".o_notebook .nav-link:contains(Odoo Implementation)",
            },
            {
                content: "Related use cases separator is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_horizontal_separator:contains(Related Use Cases)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Change Request group is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_horizontal_separator:contains(Change Request)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Configuration Change Record group is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_horizontal_separator:contains(Configuration Change Record)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Issue group is displayed",
                trigger:
                    ".o_notebook .tab-pane.active .o_horizontal_separator:contains(Issue)",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ]
    );
});
