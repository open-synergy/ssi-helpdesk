# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).
{
    "name": "Helpdesk - Project Integration",
    "version": "14.0.2.7.1",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "ssi_helpdesk",
        "ssi_project",
        "ssi_task_timebox",
        "project_stage_state",
    ],
    "data": [
        "views/project_task_views.xml",
        "views/helpdesk_type_views.xml",
        "views/helpdesk_ticket_views.xml",
    ],
    "demo": [],
    "images": [],
}
