# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk",
    "version": "14.0.2.17.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_open_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_transaction_terminate_mixin",
        "base_automation",
        "base_duration",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/policy_template_data.xml",
        "data/approval_template_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_automation_data.xml",
        "menu.xml",
        "wizards/create_ticket_from_communication_views.xml",
        "wizards/split_helpdesk_ticket_views.xml",
        "views/helpdesk_type_category_views.xml",
        "views/helpdesk_type_views.xml",
        "views/helpdesk_channel_views.xml",
        "views/helpdesk_contact_group_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_communication_views.xml",
        "views/helpdesk_resolution_documentation_type_views.xml",
    ],
    "demo": [],
}
