# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class Batch_transfer_inherit(models.Model):
    _inherit = "stock.picking.batch"

    dock = fields.Many2one('fleet.dock', string = 'Dock')
    vehicle_ids = fields.Many2one('fleet.vehicle',string = 'Vehicle')
    category_ids = fields.Many2one('fleet.vehicle.model.category',string = 'Vehicle Category')
    weight = fields.Float(string='Weight', compute = '_compute_weight',readonly=True)
    volume = fields.Float(string='Volume', compute = '_compute_volume',readonly=True)

    @api.depends("category_ids")
    def _compute_weight(self):
        for record in self:
            total = 0
            for move in record.move_ids:
                total += move.product_id.weight*move.product_qty
            if record.category_ids or record.category_ids.max_weight != 0:
                record.weight = total*100 / record.category_ids.max_weight
            else:
                record.weight = total

    @api.depends("category_ids")
    def _compute_volume(self):
        for record in self:
            total = 0
            for move in record.move_ids:
                total += move.product_id.volume*move.product_qty
            if record.category_ids or record.category_ids.max_volume != 0:
                record.volume = total*100 / record.category_ids.max_volume
            else:
                record.volume = total

    @api.depends('weight', 'volume', 'name')
    def _compute_display_name(self):
        super()._compute_display_name()
        for record in self:
            record.display_name = f"{record.name} : {record.weight:.2f}kg, {record.volume:.2f}m³"
