# -*- coding: utf-8 -*-
# from odoo import http


# class MantenimientoHector(http.Controller):
#     @http.route('/mantenimiento_hector/mantenimiento_hector', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mantenimiento_hector/mantenimiento_hector/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mantenimiento_hector.listing', {
#             'root': '/mantenimiento_hector/mantenimiento_hector',
#             'objects': http.request.env['mantenimiento_hector.mantenimiento_hector'].search([]),
#         })

#     @http.route('/mantenimiento_hector/mantenimiento_hector/objects/<model("mantenimiento_hector.mantenimiento_hector"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mantenimiento_hector.object', {
#             'object': obj
#         })

