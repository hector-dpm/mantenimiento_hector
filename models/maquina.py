# -*- coding: utf-8 -*-

from odoo import models, fields, api


class maquina(models.Model):
    _name = 'mantenimiento_hector.maquina'
    _description = 'mantenimiento_hector.maquina'

    nombre = fields.Char()
    codigo_unico = fields.Integer()
    descripcion = fields.Text()
    fecha_compra = fields.Date()
    coste_maquina = fields.Float()
    activa = fields.Boolean()
    incidencias = fields.One2many('mantenimiento_hector.incidencia', 'maquina_id')
    total_incidentes = fields.Float(compute='_compute_total_incidentes')
    ultima_incidencia = fields.Date(compute='_compute_ultima_incidencia')

    @api.depends('incidencias')
    def _compute_total_incidentes(self):
        for record in self:
            record.total_incidentes = len(record.incidencias)

    tecnico_habitual_id = fields.Many2one('mantenimiento_hector.tecnico', compute='_compute_tecnico_habitual', string='Técnico Habitual')

    @api.depends('incidencias.orden_mantenimiento_id.tecnicos_id')
    def _compute_tecnico_habitual(self):
        for record in self:
            tecnicos = []
            for incidencia in record.incidencias:
                if incidencia.orden_mantenimiento_id:
                    tecnicos.extend(incidencia.orden_mantenimiento_id.tecnicos_id.ids)
            
            if tecnicos:
                record.tecnico_habitual_id = max(set(tecnicos), key=tecnicos.count)
            else:
                record.tecnico_habitual_id = False

    @api.depends('incidencias')
    def _compute_ultima_incidencia(self):
        for record in self:
            record.ultima_incidencia = record.incidencias and record.incidencias[-1].fecha_reporte or False

