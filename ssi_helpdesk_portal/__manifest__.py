# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).
{
    "name": "Helpdesk Portal",
    "version": "14.0.2.7.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "utm",
        "portal",
        "website",
        "website_form",
        "ssi_helpdesk",
    ],
    "data": [
        # "data/website_helpdesk.xml",
        # "views/assets.xml",
        # "views/helpdesk_views.xml",
        # "views/helpdesk_templates.xml",
        "views/helpdesk_portal_templates.xml",
    ],
    "demo": [],
    "images": [],
}
