# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).

from odoo import api, models
from odoo.addons.http_routing.models.ir_http import slug


class HelpdeskTicket(models.Model):
    _name = "helpdesk_ticket"
    _inherit = [
        'helpdesk_ticket',
        'portal.mixin',
        'mail.thread.cc',
        'utm.mixin',
        'rating.mixin',
        'mail.activity.mixin',
        'website.published.mixin',
    ]

    def get_helpdesk_url(self):
        self.ensure_one()
        return "/helpdesk/%s" % slug(self)
