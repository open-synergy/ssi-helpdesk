import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-helpdesk",
    description="Meta package for open-synergy-ssi-helpdesk Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_helpdesk',
        'odoo14-addon-ssi_helpdesk_appointment',
        'odoo14-addon-ssi_helpdesk_data_requirement',
        'odoo14-addon-ssi_helpdesk_odoo_implementation',
        'odoo14-addon-ssi_helpdesk_portal',
        'odoo14-addon-ssi_helpdesk_project',
        'odoo14-addon-ssi_helpdesk_work_log',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
