# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class Batch_transfer_inherit(models.Model):
    _inherit = "stock.picking.batch"

    dock = fields.Char(string = 'Dock')
    vehicle = fields.Many2one('fleet.vehicle',string = 'Vehicle')
    vehicle_category = fields.Many2one('fleet.vehicle.model.category',string = 'Vehicle Category')
    weight = fields.Float(string='Weight', default = 30)
    volume = fields.Float(string='Volume', default = 50)
