# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': "POS Default Customer | Point of Sales Default Invoice Customer",
    'version': '15.0.0.0',
    'category': 'Point of Sale',
    'summary': 'This app allows users to set default customer on point of sales default customer on pos default customers point of sale default customer set default customer on pos default Invoice customer point of sale default invoice customer',
    'description': """ The Point of Sale Default Customer odoo app helps users to configure a default customer for their POS transactions, and when the user starts session default customer will be auto-selected on the point of sale screen, User can also change the customer if needed. This app provides a seamless and efficient way to manage default customers for your Point of Sale operations. """,
    'author': 'BrowseInfo',
    'website': "https://www.browseinfo.com",
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/pos_config.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'bi_pos_default_customer/static/src/js/models.js',
        ],
    },
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
    "live_test_url":"https://youtu.be/waB6-PgMe-Q",
    "images":['static/description/Banner.gif'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
