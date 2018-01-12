# -*- coding: utf-8 -*-
from odoo import http

# class Openlib(http.Controller):
#     @http.route('/openlib/openlib/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openlib/openlib/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openlib.listing', {
#             'root': '/openlib/openlib',
#             'objects': http.request.env['openlib.openlib'].search([]),
#         })

#     @http.route('/openlib/openlib/objects/<model("openlib.openlib"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openlib.object', {
#             'object': obj
#         })