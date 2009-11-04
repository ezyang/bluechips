"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons import tmpl_context as c
from pylons.controllers import WSGIController
from pylons.i18n import _, ungettext, N_
from pylons.templating import render_mako as render

import bluechips.lib.helpers as h
from bluechips import model
from bluechips.model import meta


class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            meta.Session.remove()

def update_sar(record, form_result):
    """
    Update a SQLAlchemy record with the results of a validated form submission
    """
    for key, value in form_result.items():
        setattr(record, key, value)

__all__ = ['c', 'h', 'render', 'model', 'meta', '_', 'ungettext', 'N_',
           'BaseController', 'update_sar']
