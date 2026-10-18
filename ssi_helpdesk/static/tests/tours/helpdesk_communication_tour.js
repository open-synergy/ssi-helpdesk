/* Copyright 2026 OpenSynergy Indonesia
 * Copyright 2026 PT. Simetri Sinergi Indonesia
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("ssi_helpdesk.helpdesk_communication_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Assertion-only step body: do not trigger the default click.
    function assertOnly() {
        // Assertion only; do not trigger the default click.
    }

    // Shared navigation block -- Flow step 1 of every IK in
    // docs/helpdesk_communication/: "Open the Helpdesk > Communications
    // menu." The Helpdesk app lands on the Tickets list, so a presence
    // gate such as `.o_list_view` would match the OLD list. The old
    // control panel is marked stale before the click and the gate waits
    // for a control panel WITHOUT the marker that shows the destination
    // action title (odoo-development-ui-test, patterns-advanced-gotchas.md
    // section T).
    function openCommunicationsList() {
        return [
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
                run: assertOnly,
            },
        ];
    }

    // Open the fixture record whose Title is shown in the list (the Title
    // column is always visible; the document number is not used because a
    // communication is numbered as soon as it is created).
    function openCommunication(title) {
        return [
            {
                content: "Open the record",
                trigger: ".o_data_row:contains(" + title + ") .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record form is displayed",
                trigger: ".o_form_view",
                run: assertOnly,
            },
        ];
    }

    // Click a statusbar button, then OK on the confirmation dialog
    // (confirm="..." on the button -- form view only).
    function clickButtonAndConfirm(name, label) {
        return [
            {
                content: "Click the " + label + " button",
                trigger: ".o_statusbar_buttons button[name='" + name + "']",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Confirm the dialog",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },
        ];
    }

    // Post-Condition assertion on the statusbar, gated on the
    // confirmation dialog being closed.
    function assertStatus(value, label) {
        return [
            {
                content: "Status is " + label,
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='" +
                    value +
                    "'].btn-primary",
                extra_trigger: "body:not(:has(.modal))",
                run: assertOnly,
            },
        ];
    }

    // IK: docs/helpdesk_communication/01-create.md
    tour.register(
        "ssi_helpdesk_helpdesk_communication_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(openCommunicationsList(), [
            // Flow 2 -- Click the New button.
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: assertOnly,
            },

            // Flow 3 -- Fill in the required fields in the header. Date
            // defaults to today and is left as-is.
            {
                content: "Select the Contact",
                trigger: ".o_field_many2one[name='partner_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour HC Create Contact",
            },
            {
                content: "Pick the Contact from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour HC Create Contact)",
                in_modal: false,
            },
            {
                content: "Fill in the Title",
                trigger: ".o_field_widget[name='title']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour HC Create Communication",
            },
            {
                // Tags is optional (IK 01-create step 4); the tour only
                // checks that the field is shown.
                content: "Tags field is shown",
                trigger: ".o_field_widget[name='global_tag_ids']",
                run: assertOnly,
            },

            // Flow 6 -- Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: assertOnly,
            },

            // Post-Condition -- A new record is created in Draft status.
            {
                content: "Status is Draft",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                run: assertOnly,
            },
        ])
    );

    // IK: docs/helpdesk_communication/02-edit.md
    tour.register(
        "ssi_helpdesk_helpdesk_communication_edit",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openCommunicationsList(),
            // Flow 2 -- Open the record to edit.
            openCommunication("Tour HC Edit Communication"),
            [
                // Flow 3 -- Click the Edit button (14.0 only).
                {
                    content: "Click the Edit button",
                    trigger: ".o_form_button_edit",
                },
                {
                    content: "Form is now editable",
                    trigger: ".o_form_view.o_form_editable",
                    run: assertOnly,
                },

                // Flow 4 -- Tags is optional; check that it is editable.
                {
                    content: "Tags field is editable",
                    trigger: ".o_field_widget[name='global_tag_ids']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: assertOnly,
                },

                // Flow 4 -- Change the Title.
                {
                    content: "Change the Title",
                    trigger: ".o_field_widget[name='title']",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Tour HC Edit Communication Changed",
                },

                // Flow 5 -- Set Waiting For on the Activities tab.
                {
                    content: "Open the Activities page",
                    trigger: ".o_notebook .nav-link:contains(Activities)",
                    extra_trigger: ".o_form_view.o_form_editable",
                },
                {
                    content: "Set Waiting For to Confirmation",
                    trigger: "select.o_field_widget[name='waiting_for']",
                    run: "text Confirmation",
                },

                // Flow 6 -- Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: assertOnly,
                },
                {
                    content: "Waiting For shows the selected value",
                    trigger:
                        ".o_form_readonly .o_field_widget[name='waiting_for']:contains('Confirmation')",
                    run: assertOnly,
                },

                // Post-Condition -- The record is updated with the new
                // values. Go back to the list and reopen the record so the
                // title is read from a genuine text node.
                {
                    content: "Go back to the list",
                    trigger:
                        ".breadcrumb-item:not(.active):contains('Helpdesk Communications')",
                },
                {
                    content: "Reopen the record",
                    trigger:
                        ".o_data_row:contains(Tour HC Edit Communication Changed) .o_data_cell:first",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Title shows the new value",
                    trigger:
                        ".o_form_readonly .o_field_widget[name='title']:contains('Tour HC Edit Communication Changed')",
                    run: assertOnly,
                },
            ]
        )
    );

    // IK: docs/helpdesk_communication/03-delete.md
    tour.register(
        "ssi_helpdesk_helpdesk_communication_delete",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openCommunicationsList(),
            // Flow 2 -- Open the record to delete.
            openCommunication("Tour HC Delete Communication"),
            [
                // Flow 3 -- Click Action > Delete.
                {
                    content: "Open the Action menu",
                    trigger: ".o_cp_action_menus button:contains(Action)",
                    // 14.0: the Action dropdown is an Owl component that
                    // does not always open on a synthetic click
                    // (odoo-development-ui-test, patterns-dialogs-and-
                    // wizards.md section I).
                    run: function () {
                        this.$anchor[0].click();
                    },
                },
                {
                    content: "Click Delete",
                    // Match the label EXACTLY -- :contains(Delete) as a
                    // substring could match another item.
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

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm deletion",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- After the delete the 14.0 form shows
                // the next record of the list, so return to the list
                // explicitly and assert the record is gone.
                {
                    content: "Return to the list",
                    trigger:
                        ".breadcrumb-item:not(.active):contains('Helpdesk Communications')",
                    extra_trigger: "body:not(:has(.modal))",
                },
                {
                    content: "Record no longer appears in the list",
                    trigger:
                        ".o_list_view:not(:has(.o_data_row:contains(Tour HC Delete Communication)))",
                    extra_trigger: ".o_list_view .o_data_row",
                    run: assertOnly,
                },
            ]
        )
    );

    // IK: docs/helpdesk_communication/07-start.md
    tour.register(
        "ssi_helpdesk_helpdesk_communication_start",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openCommunicationsList(),
            // Flow 2 -- Open the record to start.
            openCommunication("Tour HC Start Communication"),
            // Flow 3-4 -- Click Start, then OK on the dialog.
            clickButtonAndConfirm("action_open", "Start"),
            // Post-Condition -- Status changes to On Progress.
            assertStatus("open", "On Progress")
        )
    );

    // IK: docs/helpdesk_communication/09-finish.md
    tour.register(
        "ssi_helpdesk_helpdesk_communication_finish",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openCommunicationsList(),
            // Flow 2 -- Open the record to finish.
            openCommunication("Tour HC Finish Communication"),
            // Flow 3-4 -- Click Done, then OK on the dialog.
            clickButtonAndConfirm("action_done", "Done"),
            // Post-Condition -- Status changes to Done.
            assertStatus("done", "Done")
        )
    );

    // IK: docs/helpdesk_communication/12-restart.md
    tour.register(
        "ssi_helpdesk_helpdesk_communication_restart",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openCommunicationsList(),
            // Flow 2 -- Open the record to restart.
            openCommunication("Tour HC Restart Communication"),
            // Flow 3-4 -- Click Restart, then OK on the dialog.
            clickButtonAndConfirm("action_restart", "Restart"),
            // Post-Condition -- Status returns to Draft.
            assertStatus("draft", "Draft")
        )
    );

    // IK: docs/helpdesk_communication/14-reload-followers.md
    tour.register(
        "ssi_helpdesk_helpdesk_communication_reload_followers",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openCommunicationsList(),
            // Flow 2 -- Open the record whose followers will be reloaded.
            openCommunication("Tour HC Reload Communication"),
            [
                // Flow 3 -- Click Reload Followers From Ticket. The button
                // is type="object" and subscribes partners, so the gate
                // below must name a follower that cannot exist before the
                // click: the contact of the linked ticket, which is not the
                // contact of the communication
                // (patterns-advanced-gotchas.md section P).
                {
                    content: "Click Reload Followers From Ticket",
                    trigger: ".o_form_view button[name='action_reload_followers']",
                    extra_trigger: ".o_form_view.o_form_readonly",
                },
                {
                    content: "Open the followers list",
                    trigger: ".o_FollowerListMenu_buttonFollowers",
                    extra_trigger: ".o_form_view",
                },

                // Post-Condition -- The followers now include the contact
                // of the linked ticket.
                {
                    content: "The ticket contact is now a follower",
                    trigger: ".o_Follower_name:contains(Tour HC Ticket Contact)",
                    run: assertOnly,
                },
            ]
        )
    );

    // IK: docs/helpdesk_communication/15-create-ticket.md
    tour.register(
        "ssi_helpdesk_helpdesk_communication_create_ticket",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            openCommunicationsList(),
            // Flow 2 -- Open the record to convert into a ticket.
            openCommunication("Tour HC Wizard Communication"),
            [
                // Flow 3 -- Click Create Ticket. The button is
                // type="action", so its name is a numeric action id and it
                // is matched by label.
                {
                    content: "Click Create Ticket",
                    trigger: ".o_form_view button:enabled:contains('Create Ticket')",
                    extra_trigger: ".o_form_view.o_form_readonly",
                },
                {
                    content: "The wizard is displayed",
                    trigger: ".modal-title:contains(Create Ticket)",
                    in_modal: false,
                    run: assertOnly,
                },

                // Flow 4 -- Select the Category first: changing it clears
                // the Type.
                {
                    content: "Select the Category",
                    trigger: ".o_field_many2one[name='category_id'] input",
                    run: "text Tour HC Wizard Category",
                },
                {
                    content: "Pick the Category from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour HC Wizard Category)",
                    in_modal: false,
                },
                {
                    content: "Select the Type",
                    trigger: ".o_field_many2one[name='type_id'] input",
                    run: "text Tour HC Wizard Type",
                },
                {
                    content: "Pick the Type from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour HC Wizard Type)",
                    in_modal: false,
                },

                // Flow 5-6 -- Click Confirm on the wizard, then OK on the
                // confirmation dialog.
                {
                    content: "Confirm the wizard",
                    trigger: ".modal-footer button[name='action_confirm']",
                },
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- The new ticket is opened and shows the
                // selected Type.
                {
                    content: "The new ticket is displayed",
                    trigger:
                        ".o_form_view .o_field_widget[name='type_id']:contains(Tour HC Wizard Type)",
                    extra_trigger: "body:not(:has(.modal))",
                    run: assertOnly,
                },
            ]
        )
    );
});
