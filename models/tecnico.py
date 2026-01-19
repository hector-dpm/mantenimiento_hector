# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tecnico(models.Model):
    _name = 'mantenimiento_hector.tecnico'
    _description = 'mantenimiento_hector.tecnico'

    nombre = fields.Char()
    telefono = fields.Integer()
    email = fields.Char()

    nivel_practica = fields.Selection([
        ('junior', 'Junior'),
        ('medio', 'Medio'),
        ('senior', 'Senior'),
    ], default='junior')

    activo = fields.Boolean()

    ordenes_id = fields.Many2many('mantenimiento_hector.orden_mantenimiento', 'tecnico_id')

    total_ordenes = fields.Integer(compute='_compute_total_ordenes')

    @api.depends('ordenes_id')
    def _compute_total_ordenes(self):
        for record in self:
            record.total_ordenes = len(record.ordenes_id)