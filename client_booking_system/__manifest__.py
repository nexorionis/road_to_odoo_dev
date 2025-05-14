# -*- coding: utf-8 -*-
{
    'name' : 'Client Booking System',
    'version' : '1.0',
    'summary': 'Booking',
    'sequence': 100,
    'description': """
            Booking System
    """,
    'category': 'All',
    'website': 'https://www.odoo.com',
    'depends': ['base',],
    'data': [
        'security/ir.model.access.csv',
        'views/booking_system_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
