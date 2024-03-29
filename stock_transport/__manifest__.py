# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Transport Management System',
    'version' : '1.0',
    'category': 'stock_transport',
    'summary':'A Transport Management System',
    'depends': ['base','stock','fleet','stock_picking_batch'],
    'data':[
        'views/batch_transfer_inherit_view.xml',
        'views/fleet_category_inherit_view.xml',
        'views/stock_picking_batch_graph.xml'
    ],
    'installable':True,
    'application':True,
    'license': 'LGPL-3'
}
