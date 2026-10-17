/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk_operating_unit.helpdesk_communication_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/helpdesk_communication/01-create.md
    tour.register(
        "ssi_helpdesk_operating_unit_ou81_helpdesk_communication_create",
        {
            test: true,
            url: "/web",
        },
        [
            // Base Flow 1 -- Open the Helpdesk > Communications menu. The old
            // control panel is marked stale before the click so the gate
            // waits for the destination action title.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Helpdesk app",
                trigger: '.o_app[data-menu-xmlid="ssi_helpdesk.menu_root_helpdesk"]',
            },
            {
                content: "Open the Communications menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_communication_menu"]',
                run: function (actions) {
                    // Instrumentation only: dies together with the old
                    // controller.
                    $(".o_control_panel").addClass("oe_tour_stale");
                    actions.click();
                },
            },
            {
                content: "Communications list is displayed",
                trigger:
                    ".o_control_panel:not(.oe_tour_stale) .breadcrumb-item.active:contains(Helpdesk Communications)",
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

            // Delta Flow (anchor: base Flow 4) -- the Operating Unit field
            // is shown in the header.
            {
                content: "Operating Unit field is displayed",
                trigger:
                    ".o_form_view.o_form_editable .o_field_widget[name='operating_unit_id']",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ]
    );
});
