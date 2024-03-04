# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class Fleet_category_inherit(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string = 'Max Weight (Kg)')
    max_volume = fields.Float(string = 'Max Volume (m³)')

    def _compute_display_name(self):
        super()._compute_display_name()
        for record in self:
            record.display_name = record.name+" ("+str(record.max_weight)+"kg, "+str(record.max_volume)+"m³)"
