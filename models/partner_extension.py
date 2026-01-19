# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    es_tecnico_mantenimiento = fields.Boolean(string="Es Técnico de Mantenimiento")
