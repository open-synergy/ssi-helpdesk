# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import http
from odoo.http import request

from odoo.addons.website_form.controllers.main import WebsiteForm


class HelpdeskPortal(http.Controller):
    """Website controller for public helpdesk ticket pages."""

    @http.route(
        ["/helpdesk/", '/helpdesk/<model("helpdesk_ticket"):ticket>'],
        type="http",
        auth="public",
        website=True,
        sitemap=True,
    )
    def ssi_helpdesk_portal(self, ticket=None, **kwargs):
        """Render the public helpdesk page at ``/helpdesk/``.

        Route: ``/helpdesk/`` and ``/helpdesk/<ticket>``. Passes the
        selected ticket and all tickets (for the breadcrumb index) to
        the ``ssi_helpdesk_portal.ticket`` template.

        :param ticket: optional ``helpdesk_ticket`` record from the URL
        :param kwargs: extra request parameters (``search`` is ignored)
        :return: rendered response of the ticket template
        """
        kwargs.get("search")
        # For breadcrumb index: get all ticket
        tickets = request.env["helpdesk_ticket"].search([], order="id asc")
        result = {"ticket": ticket}
        # For breadcrumb index: get all ticket
        result["tickets"] = tickets
        return request.render("ssi_helpdesk_portal.ticket", result)


class WebsiteForm(WebsiteForm):
    """Website form controller that fills helpdesk ticket defaults."""

    def _handle_website_form(self, model_name, **kwargs):
        """Handle a website form submission with ticket context values.

        Injects the website flag, title, description, attachments, the
        current user partner and the admin user into the request context
        before delegating to the parent implementation.

        :param model_name: technical name of the model being created
        :param kwargs: submitted form fields
        :return: JSON response produced by the parent implementation
        """
        context = request.env.context.copy()
        attachments = []
        for key, value in kwargs.items():
            if key[:11] == "attachments":
                attachments.append(value)
        values = {
            "from_website": True,
            "title": kwargs.get("title"),
            "partner_id": request.env.user.partner_id.id,
            "user_id": request.env.ref("base.user_admin").id,
            "description": kwargs.get("description"),
            "attachments": attachments,
        }
        context.update(values)
        request.env.context = context
        return super(WebsiteForm, self)._handle_website_form(model_name, **kwargs)
