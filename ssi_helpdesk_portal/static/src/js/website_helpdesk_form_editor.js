odoo.define("ssi_helpdesk_portal.form", function (require) {
    "use strict";

    var FormEditorRegistry = require("website_form.form_editor_registry");

    FormEditorRegistry.add("create_ticket", {
        formFields: [
            {
                type: "char",
                required: true,
                name: "title",
                string: "Title",
            },
            {
                type: "char",
                name: "description",
                string: "Description",
            },
            {
                type: "binary",
                custom: true,
                name: "Attachment",
            },
        ],
        successPage: "/your-ticket-has-been-submitted",
    });
});
