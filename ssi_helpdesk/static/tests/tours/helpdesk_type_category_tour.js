/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk.helpdesk_type_category_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/helpdesk_type_category/01-create.md
    tour.register(
        "ssi_helpdesk_helpdesk_type_category_create",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Helpdesk > Configuration > Ticket > Categories
            // menu. The "Ticket" level is a level-3 grouping header without
            // its own action or data-menu-xmlid, so it has no step.
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
                content: "Open the Categories menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_type_category_menu"]',
            },
            {
                content: "Categories list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Type Categories)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Click the New button.
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

            // Flow 3 — Fill in the required fields.
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR-HDC-CREATE",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                run: "text /",
            },

            // Flow 4 — Click Save.
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

            // Post-Condition — A new record is created and active.
            {
                content: "The record is active (no Archived ribbon)",
                trigger: ".o_form_view:not(:has(.ribbon:visible:contains(Archived)))",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_type_category/02-edit.md
    tour.register(
        "ssi_helpdesk_helpdesk_type_category_edit",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Helpdesk > Configuration > Ticket > Categories
            // menu. The "Ticket" level is a level-3 grouping header without
            // its own action or data-menu-xmlid, so it has no step.
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
                content: "Open the Categories menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_type_category_menu"]',
            },
            {
                content: "Categories list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Type Categories)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Find and open the record to edit.
            {
                content: "Open the record",
                trigger: ".o_data_row:contains(TOUR-HDC-EDIT) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            {
                content: "Click the Edit button",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Form is now editable",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 3 — Change the required fields.
            {
                content: "Change the Name",
                trigger: ".o_field_widget[name='name']",
                run: "text TOUR-HDC-EDIT-UPDATED",
            },

            // Flow 4 — Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // Post-Condition — The record is updated with the new values.
            {
                content: "Go back to the list",
                trigger: ".breadcrumb-item:not(.active):contains(Type Categories)",
            },
            {
                content: "The updated name is shown in the list",
                trigger: ".o_data_row:contains(TOUR-HDC-EDIT-UPDATED)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_type_category/03-delete.md
    tour.register(
        "ssi_helpdesk_helpdesk_type_category_delete",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Helpdesk > Configuration > Ticket > Categories
            // menu. The "Ticket" level is a level-3 grouping header without
            // its own action or data-menu-xmlid, so it has no step.
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
                content: "Open the Categories menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_type_category_menu"]',
            },
            {
                content: "Categories list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Type Categories)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Select the record.
            {
                content: "Select the record",
                trigger:
                    ".o_data_row:contains(TOUR-HDC-DELETE) .o_list_record_selector input",
                extra_trigger: ".o_list_view",
            },

            // Flow 3 — Click Action > Delete.
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
            },
            {
                content: "Click Delete",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $item = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Delete";
                        }
                    );
                    $item[0].click();
                },
            },

            // Flow 4 — Click OK to confirm.
            {
                content: "Confirm",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // Post-Condition.
            {
                content: "The record no longer appears in the list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(TOUR-HDC-DELETE)))",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_type_category/04-deactivate.md
    tour.register(
        "ssi_helpdesk_helpdesk_type_category_deactivate",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Helpdesk > Configuration > Ticket > Categories
            // menu. The "Ticket" level is a level-3 grouping header without
            // its own action or data-menu-xmlid, so it has no step.
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
                content: "Open the Categories menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_type_category_menu"]',
            },
            {
                content: "Categories list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Type Categories)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Select the record.
            {
                content: "Select the record",
                trigger:
                    ".o_data_row:contains(TOUR-HDC-DEACTIVATE) .o_list_record_selector input",
                extra_trigger: ".o_list_view",
            },

            // Flow 3 — Click Action > Archive.
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
            },
            {
                content: "Click Archive",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $item = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Archive";
                        }
                    );
                    $item[0].click();
                },
            },

            // Flow 4 — Click OK to confirm.
            {
                content: "Confirm",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // Post-Condition.
            {
                content: "The record no longer appears in the default list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(TOUR-HDC-DEACTIVATE)))",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_type_category/05-activate.md
    tour.register(
        "ssi_helpdesk_helpdesk_type_category_activate",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Helpdesk > Configuration > Ticket > Categories
            // menu. The "Ticket" level is a level-3 grouping header without
            // its own action or data-menu-xmlid, so it has no step.
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
                content: "Open the Categories menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_type_category_menu"]',
            },
            {
                content: "Categories list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Type Categories)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Enable the Archived filter.
            {
                content: "Open the Filters menu",
                trigger: ".o_search_options .o_filter_menu button",
            },
            {
                content: "Enable the Archived filter",
                trigger: ".o_filter_menu .dropdown-item:contains(Archived)",
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Archived filter is active",
                trigger:
                    ".o_filter_menu .dropdown-item:contains(Archived)[aria-checked='true']",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 3 — Select the record to reactivate.
            {
                content: "Select the record",
                trigger:
                    ".o_data_row:contains(TOUR-HDC-ACTIVATE) .o_list_record_selector input",
                extra_trigger: ".o_list_view",
            },

            // Flow 4 — Click Action > Unarchive. No confirmation dialog.
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
            },
            {
                content: "Click Unarchive",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $item = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Unarchive";
                        }
                    );
                    $item[0].click();
                },
            },
            // Unarchiving is an async write + list refresh: wait for the
            // record to leave the Archived-filtered list before touching
            // the filter again.
            {
                content: "The record no longer appears in the Archived list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(TOUR-HDC-ACTIVATE)))",
                run: function () {
                    // Assertion only.
                },
            },

            // Post-Condition — The record appears in the default list again.
            {
                content: "Disable the Archived filter",
                trigger: ".o_search_options .o_filter_menu button",
            },
            {
                content: "Toggle the Archived filter off",
                trigger: ".o_filter_menu .dropdown-item:contains(Archived)",
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "The record appears again in the default list",
                trigger: ".o_data_row:contains(TOUR-HDC-ACTIVATE)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
