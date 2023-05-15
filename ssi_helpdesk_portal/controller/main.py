# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0-standalone.html).

from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm


class HelpdeskPortal(http.Controller):

    def _get_partner_data(self):
        partner = request.env.user.partner_id
        partner_values = {}
        if partner != request.website.user_id.sudo().partner_id:
            partner_values['name'] = partner.name
            partner_values['email'] = partner.email
        return partner_values

    @http.route(['/helpdesk/', '/helpdesk/<model("helpdesk_ticket"):ticket>'], type='http', auth="public", website=True,
                sitemap=True)
    def ssi_helpdesk_portal(self, ticket=None, **kwargs):
        search = kwargs.get('search')
        # For breadcrumb index: get all ticket
        tickets = request.env['helpdesk_ticket'].search([], order="id asc")
        result = {'ticket': ticket}
        # For breadcrumb index: get all ticket
        result['tickets'] = tickets
        result['default_partner_values'] = self._get_partner_data()
        return request.render("ssi_helpdesk_portal.ticket", result)
