# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class Fleet_dock(models.Model):
    _name = "fleet.dock"

    name = fields.Char(string = 'name')