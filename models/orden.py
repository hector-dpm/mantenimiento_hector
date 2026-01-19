# -*- coding: utf-8 -*-

from odoo import models, fields, api


class orden_mantenimiento(models.Model):
    _name = 'mantenimiento_hector.orden_mantenimiento'
    _description = 'mantenimiento_hector.orden_mantenimiento'

    nombre = fields.Char()

    incidencia_id = fields.Many2one('mantenimiento_hector.incidencia', string='Incidencia')

    tecnicos_id = fields.Many2many('mantenimiento_hector.tecnico', 'orden_tecnico_rel', 'orden_id', 'tecnico_id', string='Técnicos')

    materiales_id = fields.One2many('mantenimiento_hector.material', 'orden_id', string='Materiales')

    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
    ], default='pendiente')
    
    duracion = fields.Integer(string="Duración (Días)", compute='_compute_duracion', store=True)

    @api.depends('fecha_inicio', 'fecha_fin')
    def _compute_duracion(self):
        for record in self:
            if record.fecha_inicio and record.fecha_fin:
                record.duracion = (record.fecha_fin - record.fecha_inicio).days
            else:
                record.duracion = 0
    



