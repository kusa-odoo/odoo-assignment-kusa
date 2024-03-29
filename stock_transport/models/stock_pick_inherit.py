# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class Batch_transfer_inherit(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float('Volume', compute='_compute_volume')

    def _compute_volume(self):
        for record in self:
            total = 0
            for move in record.move_ids:
                total += move.product_id.volume*move.product_qty
            record.volume = total