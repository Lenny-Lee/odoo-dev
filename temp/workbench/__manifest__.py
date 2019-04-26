# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'workbench',
    'version': '10.1.01',
    'summary': '工作台',
    'sequence': 3,
    'description': """
模块说明
====================



   """,
    'category': '',
    'website': '',
    'images': [],
    'depends': [ 'base', 'web'],
    'data': [
        'security/workbench_security.xml',
        'security/ir.model.access.csv',
        'views/shortcut_view.xml',
        'views/chart_view.xml',
        'views/workbench_view.xml',
    ],
    'demo': [
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
