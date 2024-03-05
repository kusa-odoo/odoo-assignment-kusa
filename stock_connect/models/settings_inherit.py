# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class Settings_inherit(models.TransientModel):
    _inherit = "res.config.settings"

    module_stock_transport = fields.Boolean(string='Dispatch Management System')
