// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_helpdesk_elearning.helpdesk_ticket_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/helpdesk_ticket/02-edit.md (delta -- Additional Fields,
    // Modified Flow). Navigation (open menu, open record, Edit) is taken
    // from the base IK ssi_helpdesk/docs/helpdesk_ticket/02-edit.md Flow
    // steps 1-3. The delta assertion comes from this module's own IK: the
    // line form of the Resolution Documentation(s) tab shows the Course
    // and Content fields. The tour stops there; it does not fill or save.
    tour.register(
        "ssi_helpdesk_elearning_helpdesk_ticket_edit",
        {
            test: true,
            url: "/web",
        },
        [
            // Base Flow 1 -- Open the Helpdesk > Tickets menu. Tickets is
            // the landing action of the app, so a stale-marker gate is
            // used instead of a presence gate.
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

            // Base Flow 2 -- Find and open the record to edit.
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(Tour EL76 Edit Ticket) .o_data_cell:first",
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

            // Modified Flow -- open the Resolution Documentation(s) tab.
            {
                content: "Open the Resolution Documentation(s) tab",
                trigger: ".o_notebook .nav-link:contains(Resolution Documentation)",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            // Modified Flow -- click Add a line.
            {
                content: "Click Add a line",
                trigger: ".tab-pane.active .o_field_x2many_list_row_add a",
            },
            // Delta assertion -- Course and Content are on the line form.
            // The line form opens in a dialog. The first step also waits
            // for it: the Course field exists only in the dialog (the
            // list column set has no Course), and 14.0 in-modal triggers
            // are written relative to the modal content, not prefixed
            // with .modal.
            {
                content: "Course field is visible on the line form",
                trigger: ".o_field_widget[name='course_id']",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
            {
                content: "Content field is visible on the line form",
                trigger: ".o_field_widget[name='content_id']",
                run: function () {
                    // Assertion only; do not trigger the default click.
                },
            },
        ]
    );
});
