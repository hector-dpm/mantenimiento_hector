# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class incidencia(models.Model):
    _name = 'mantenimiento_hector.incidencia'
    _description = 'mantenimiento_hector.incidencia'

    nombre = fields.Char()

    maquina_id = fields.Many2one('mantenimiento_hector.maquina', string='Maquina')
    descripcion = fields.Text()

    prioridad = fields.Selection([('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], default='baja')
    
    estado = fields.Selection([('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('completada', 'Completada')], default='pendiente')
    
    fecha_reporte = fields.Date()
    fecha_resolucion = fields.Date()

    horas_duracion = fields.Float()

    orden_mantenimiento_id = fields.Many2one('mantenimiento_hector.orden_mantenimiento', string='Orden de Mantenimiento')

    @api.model
    def create(self, vals):
        if not vals.get('nombre'):
            vals['nombre'] = 'Incidencia Automática - ' + fields.Date.today().strftime('%Y-%m-%d')
        return super(incidencia, self).create(vals)

    @api.constrains('horas_duracion')
    def _check_horas_duracion(self):
        for record in self:
            if record.horas_duracion < 0:
                raise ValidationError("Las horas de duración no pueden ser negativas.")


    
    


