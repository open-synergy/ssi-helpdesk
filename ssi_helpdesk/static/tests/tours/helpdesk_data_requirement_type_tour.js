/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk.helpdesk_data_requirement_type_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block -- Flow step 1 of every IK in
    // docs/helpdesk_data_requirement_type/: "Open the Helpdesk > Configuration > Data Requirement Types menu."
    // Any intermediate grouping header (menuitem without an action) has no
    // step of its own (odoo-development-ui-test, patterns.md section A).
    function openList() {
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
                content: "Open the Data Requirement Types menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_helpdesk.helpdesk_data_requirement_type_menu"]',
            },
            {
                // Gate: wait for the target action to actually be mounted,
                // not just any list view left over from the landing action.
                content: "Data Requirement Types list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Data Requirement Types)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/helpdesk_data_requirement_type/01-create.md
    tour.register(
        "ssi_helpdesk_helpdesk_data_requirement_type_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(openList(), [
            // Flow 2 -- Click the New button. (14.0: "Create")
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

            // Flow 3 -- Fill in the required Name and Code fields.
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour HDR Req Create",
            },
            {
                content: "Fill in Code with /",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text /",
            },

            // Flow 4 -- Note tab: only the tab render is verified.
            {
                content: "Open the Note tab",
                trigger: ".o_notebook .nav-link:contains(Note)",
            },
            {
                content: "Note field is displayed",
                trigger: ".o_field_widget[name='note']",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 5 -- Inline Action: click Generate Code to auto-assign
            // the code left as "/" from the sequence.template prepared in
            // setUpClass.
            {
                content: "Click the Generate Code button",
                trigger: ".o_statusbar_buttons button[name='action_generate_code']",
                extra_trigger: ".o_form_view",
            },
            {
                // Gate: the object button auto-saves the still-new record
                // before running the method, so the breadcrumb keeps
                // reading "New" until that save lands (patterns.md
                // section P).
                content: "Record is saved by Generate Code",
                trigger: ".o_control_panel .breadcrumb-item.active:not(:contains(New))",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 6 -- Click Save.
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

            // Post-Condition -- A new record is created and shown in the
            // list.
            {
                content:
                    "Click the Data Requirement Types breadcrumb to return to the list",
                trigger:
                    ".breadcrumb-item.o_back_button a:contains(Data Requirement Types)",
            },
            {
                content: "New record is shown in the list",
                trigger: ".o_list_view .o_data_row:contains(Tour HDR Req Create)",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/helpdesk_data_requirement_type/02-edit.md
    tour.register(
        "ssi_helpdesk_helpdesk_data_requirement_type_edit",
        {
            test: true,
            url: "/web",
        },
        [].concat(openList(), [
            // Flow 2 -- Find and open the record to edit.
            {
                content: "Open the record",
                trigger: ".o_data_row:contains(Tour HDR Req Edit) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 3 -- Click the Edit button. (14.0 only -- the form
            // opens directly editable on 16.0+)
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

            // Flow 4 -- Change the Name to a value different from the
            // fixture's, so the Post-Condition proves the change landed.
            // Flow 5 (reassigning Code) is optional and skipped here.
            {
                content: "Change the Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour HDR Req Edited",
            },

            // Flow 6 -- Click Save.
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

            // Post-Condition -- The record is updated with the new values.
            {
                content: "Go back to the list",
                trigger:
                    ".breadcrumb-item:not(.active):contains('Data Requirement Types')",
            },
            {
                content: "Renamed record is shown in the list",
                trigger: ".o_list_view .o_data_row:contains(Tour HDR Req Edited)",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/helpdesk_data_requirement_type/03-delete.md
    tour.register(
        "ssi_helpdesk_helpdesk_data_requirement_type_delete",
        {
            test: true,
            url: "/web",
        },
        [].concat(openList(), [
            // Flow 2 -- Open the record to delete.
            {
                content: "Open the record",
                trigger: ".o_data_row:contains(Tour HDR Req Delete) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },

            // Flow 3 -- Click Action > Delete.
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
                // 14.0: the Action dropdown is an Owl component that does
                // not always open on a synthetic click (patterns.md
                // section I).
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Click Delete",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $delete = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Delete";
                        }
                    );
                    $delete[0].click();
                },
            },

            // Flow 4 -- Click OK to confirm.
            {
                content: "Confirm deletion",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // Flow 5 -- Click the breadcrumb to return to the list.
            {
                content: "Click the Data Requirement Types breadcrumb",
                trigger:
                    ".breadcrumb-item.o_back_button a:contains(Data Requirement Types)",
            },

            // Post-Condition -- The record is permanently removed.
            {
                content: "Record no longer appears in the list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(Tour HDR Req Delete)))",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/helpdesk_data_requirement_type/04-deactivate.md
    tour.register(
        "ssi_helpdesk_helpdesk_data_requirement_type_deactivate",
        {
            test: true,
            url: "/web",
        },
        [].concat(openList(), [
            // Flow 2 -- Select the record to deactivate (checkbox).
            {
                content: "Select the record to deactivate",
                trigger:
                    ".o_data_row:contains(Tour HDR Req Deactivate) .o_list_record_selector input",
                extra_trigger: ".o_list_view",
                run: "click",
            },

            // Flow 3 -- Click Action > Archive.
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Click Archive",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $archive = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Archive";
                        }
                    );
                    $archive[0].click();
                },
            },

            // Flow 4 -- Click OK to confirm. Archive (unlike Unarchive)
            // wraps its callback in Dialog.confirm at 14.0 (patterns.md
            // sections G/J).
            {
                content: "Confirm archiving",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // Post-Condition -- The record no longer appears in the
            // default (active) list view.
            {
                content: "Record no longer appears in the active list",
                trigger:
                    ".o_list_view:not(:has(.o_data_row:contains(Tour HDR Req Deactivate)))",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/helpdesk_data_requirement_type/05-activate.md
    tour.register(
        "ssi_helpdesk_helpdesk_data_requirement_type_activate",
        {
            test: true,
            url: "/web",
        },
        [].concat(openList(), [
            // Flow 2 -- Enable the Archived filter in the search bar.
            {
                content: "Open the Filters menu",
                trigger: ".o_filter_menu .o_dropdown_toggler_btn",
                // 14.0: the Filters dropdown is an Owl component that does
                // not always open on a synthetic click (patterns.md
                // sections I/J).
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Enable the Archived filter",
                trigger: ".o_filter_menu .o_menu_item a:contains(Archived)",
                run: function () {
                    this.$anchor[0].click();
                },
            },

            // Flow 3 -- Select the record to reactivate (checkbox).
            {
                content: "Select the record to reactivate",
                trigger:
                    ".o_data_row:contains(Tour HDR Req Activate) .o_list_record_selector input",
                run: "click",
            },

            // Flow 4 -- Click Action > Unarchive. At 14.0 core only
            // Archive is wrapped in Dialog.confirm; Unarchive runs
            // directly, so there is no confirmation dialog step.
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
                run: function () {
                    this.$anchor[0].click();
                },
            },
            {
                content: "Click Unarchive",
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $unarchive = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Unarchive";
                        }
                    );
                    $unarchive[0].click();
                },
            },

            // Post-Condition -- The record is restored and appears again
            // in the default (active) list view.
            {
                content: "Record appears again in the active list",
                trigger: ".o_list_view .o_data_row:contains(Tour HDR Req Activate)",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );
});
