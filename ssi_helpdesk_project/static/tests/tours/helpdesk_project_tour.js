/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk_project.helpdesk_project_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Navigation shared with docs/helpdesk_type/01-create.md of
    // ssi_helpdesk: "Open the Helpdesk > Configuration > Ticket > Types
    // menu". The "Ticket" level is a level-3 grouping header without its
    // own action or data-menu-xmlid, so it has no step.
    function openTypesList() {
        return [
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
        ];
    }

    // Navigation shared with docs/helpdesk_ticket/*.md of ssi_helpdesk.
    // Tickets is the landing action of the Helpdesk app, so clicking it
    // reloads an identical action: a stale-marker gate is used instead of
    // a presence gate.
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

    // Navigation shared with docs/project_task/*.md of ssi_project.
    function openTasksList() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Project app",
                trigger: '.o_app[data-menu-xmlid="project.menu_main_pm"]',
            },
            {
                content: "Open the Tasks menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="project.menu_project_management"]',
            },
            {
                content: "Tasks list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Tasks)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/helpdesk_type/01-create.md
    tour.register(
        "ssi_helpdesk_project_pj80_helpdesk_type_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Base Flow 1 -- Open the Types menu.
            openTypesList(),
            [
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
                        // Assertion only.
                    },
                },

                // Base Flow 3 -- Fill in the required fields.
                {
                    content: "Fill in Name",
                    trigger: ".o_field_widget[name='name']",
                    run: "text PJ80-TYPE-CREATE",
                },
                {
                    content: "Fill in Code",
                    trigger: ".o_field_widget[name='code']",
                    run: "text /",
                },
                {
                    content: "Select the Category",
                    trigger: ".o_field_many2one[name='category_id'] input",
                    run: "text PJ80 Category",
                },
                {
                    content: "Pick the Category from the dropdown",
                    trigger: ".ui-autocomplete .ui-menu-item a:contains(PJ80 Category)",
                },

                // Delta Modified Flow -- the Project tab.
                {
                    content: "Project tab is displayed",
                    trigger: ".o_notebook .nav-link:contains(Project)",
                },
                {
                    content: "Tick Need Task",
                    trigger: ".o_field_widget[name='need_task'] input",
                    run: "click",
                },
                {
                    content: "Add a task template line",
                    trigger:
                        ".o_field_widget[name='task_ids'] .o_field_x2many_list_row_add a",
                },
                {
                    content: "Fill in the Task Summary",
                    trigger: ".o_selected_row .o_field_widget[name='title']",
                    run: "text PJ80-TEMPLATE-CREATE",
                },

                // Base Flow 4 -- Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Delta Additional Post-Condition -- the template is kept.
                {
                    content: "The task template is listed",
                    trigger:
                        ".o_field_widget[name='task_ids'] .o_data_row:contains(PJ80-TEMPLATE-CREATE)",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/helpdesk_ticket/09-create-task.md
    tour.register(
        "ssi_helpdesk_project_pj80_helpdesk_ticket_create_task",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Helpdesk > Tickets menu.
            openTicketsList(),
            [
                // Flow 2 -- Find and open the ticket.
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(PJ80 Task Ticket) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Record form is displayed",
                    trigger: ".o_form_view",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Flow 3 -- Open the Tasks tab.
                {
                    content: "Open the Tasks tab",
                    trigger: ".o_notebook .nav-link:contains(Tasks)",
                },

                // Flow 4 -- Click the Create button.
                {
                    content: "Click the Create button",
                    trigger: ".o_form_view button[name='action_create_task']",
                },

                // Post-Condition -- the gate names the template task, which
                // cannot be listed before the button runs.
                {
                    content: "The task from the template is listed",
                    trigger:
                        ".o_field_widget[name='task_ids'] .o_data_row:contains(PJ80-TEMPLATE-TASK)",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/project_task/02-edit.md
    tour.register(
        "ssi_helpdesk_project_pj80_project_task_open_ticket",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Base Flow 1 -- Open the Project > Tasks menu.
            openTasksList(),
            [
                // Base Flow 2 -- Find and open the record.
                {
                    content: "Open the record",
                    trigger:
                        ".o_data_row:contains(PJ80-LINKED-TASK) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Record form is displayed",
                    trigger: ".o_form_view",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Delta Related Views -- the Tickets tab.
                {
                    content: "Open the Tickets tab",
                    trigger: ".o_notebook .nav-link:contains(Tickets)",
                },
                {
                    content: "Click the Open button",
                    trigger: ".o_form_view button[name='action_open_ticket']",
                },
                {
                    content: "The Helpdesk Tickets list is displayed",
                    trigger:
                        ".o_control_panel .breadcrumb-item.active:contains(Helpdesk Tickets)",
                    extra_trigger: ".o_list_view",
                    run: function () {
                        // Assertion only.
                    },
                },
                {
                    content: "The linked ticket is listed",
                    trigger: ".o_data_row:contains(PJ80 Linked Ticket)",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );
});
