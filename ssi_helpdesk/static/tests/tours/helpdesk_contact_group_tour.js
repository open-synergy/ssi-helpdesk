odoo.define("ssi_helpdesk.helpdesk_contact_group_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/helpdesk_contact_group/01-create.md
    tour.register(
        "ssi_helpdesk_helpdesk_contact_group_create",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contact Groups menu
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
                content: "Open the Contact Groups menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_contact_group_menu"]',
            },
            {
                content: "Helpdesk Contact Groups list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Helpdesk Contact Groups)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Click the New button
            {
                content: "Click New",
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

            // Flow 3 — Fill in the required fields
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Contact Group Create",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text /",
            },
            {
                content: "Select the Commercial Contact",
                trigger: ".o_field_many2one[name='commercial_contact_id'] input",
                run: "text TOUR HDG Company",
            },
            {
                content: "Pick the Commercial Contact from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR HDG Company)",
                in_modal: false,
            },
            {
                content: "Select a Contact",
                trigger: ".o_field_many2manytags[name='contact_ids'] input",
                run: "text TOUR HDG Contact",
            },
            {
                content: "Pick the Contact from the dropdown",
                trigger: ".ui-autocomplete .ui-menu-item a:contains(TOUR HDG Contact)",
                in_modal: false,
            },

            // Flow 5 — Click Save
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // Post-Condition — record is created and active
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_contact_group/02-edit.md
    tour.register(
        "ssi_helpdesk_helpdesk_contact_group_edit",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contact Groups menu
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
                content: "Open the Contact Groups menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_contact_group_menu"]',
            },
            {
                content: "Helpdesk Contact Groups list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Helpdesk Contact Groups)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Find and open the record to edit
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(TOUR Contact Group Edit) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record is open",
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

            // Flow 3 — Change the required fields
            {
                content: "Change the Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Contact Group Edited",
            },

            // Flow 5 — Click Save
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // Post-Condition — the record is updated with the new values
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_contact_group/03-delete.md
    tour.register(
        "ssi_helpdesk_helpdesk_contact_group_delete",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contact Groups menu
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
                content: "Open the Contact Groups menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_contact_group_menu"]',
            },
            {
                content: "Helpdesk Contact Groups list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Helpdesk Contact Groups)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Select the record to delete
            {
                content: "Select the record",
                trigger:
                    ".o_data_row:contains(TOUR Contact Group Delete) .o_list_record_selector input",
                extra_trigger: ".o_list_view",
            },

            // Flow 3 — Click Action > Delete
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

            // Flow 4 — Click OK to confirm
            {
                content: "Confirm deletion",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // Post-Condition — the record no longer appears in the list
            {
                content: "Record is removed from the list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(TOUR Contact Group Delete)))",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_contact_group/04-deactivate.md
    tour.register(
        "ssi_helpdesk_helpdesk_contact_group_deactivate",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contact Groups menu
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
                content: "Open the Contact Groups menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_contact_group_menu"]',
            },
            {
                content: "Helpdesk Contact Groups list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Helpdesk Contact Groups)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Select the record to deactivate
            {
                content: "Select the record",
                trigger:
                    ".o_data_row:contains(TOUR Contact Group Deactivate) .o_list_record_selector input",
                extra_trigger: ".o_list_view",
            },

            // Flow 3 — Click Action > Archive
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

            // Flow 4 — Click OK to confirm
            {
                content: "Confirm archiving",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // Post-Condition — the record no longer appears in the default list view
            {
                content: "Record is removed from the default list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(TOUR Contact Group Deactivate)))",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );

    // IK: docs/helpdesk_contact_group/05-activate.md
    tour.register(
        "ssi_helpdesk_helpdesk_contact_group_activate",
        {
            test: true,
            url: "/web",
        },
        [
            // Flow 1 — Open the Contact Groups menu
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
                content: "Open the Contact Groups menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_contact_group_menu"]',
            },
            {
                content: "Helpdesk Contact Groups list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Helpdesk Contact Groups)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 2 — Enable the Archived filter
            {
                content: "Open the Filters menu",
                trigger: ".o_search_options .o_filter_menu button",
                run: function () {
                    this.$anchor[0].click();
                },
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
                trigger: ".o_facet_values:contains(Archived)",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 3 — Select the record to reactivate
            {
                content: "Select the record",
                trigger:
                    ".o_data_row:contains(TOUR Contact Group Activate) .o_list_record_selector input",
                extra_trigger: ".o_list_view",
            },

            // Flow 4 — Click Action > Unarchive
            // Unarchive has NO confirmation dialog (list_controller.js:490) — do not
            // wait for a modal after this click.
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

            // Post-Condition — the record is restored and appears in the default list
            {
                content: "Record is restored to the default list",
                trigger:
                    ".o_list_view .o_data_row:contains(TOUR Contact Group Activate)",
                run: function () {
                    // Assertion only.
                },
            },
        ]
    );
});
