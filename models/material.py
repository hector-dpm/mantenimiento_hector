# -*- coding: utf-8 -*-

from odoo import models, fields, api


class material(models.Model):
    _name = 'mantenimiento_hector.material'
    _description = 'mantenimiento_hector.material'

    nombre = fields.Char()

    cantidad = fields.Float()

    precio_unidad = fields.Float()

    orden_id = fields.Many2one('mantenimiento_hector.orden_mantenimiento', string='Orden de Mantenimiento')

    total = fields.Float(compute='_compute_total')

    @api.depends('cantidad', 'precio_unidad')
    def _compute_total(self):
        for record in self:
            record.total = record.cantidad * record.precio_unidad

    

   

