# -*- coding: utf-8 -*-
{
    'name': "Open Library",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ahmet Selim Konuk",
    'website': "http://www.metglobal.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/openlib.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/genre_demo.xml',
        'demo/language_demo.xml',
        'demo/partner_demo.xml',
        'demo/book_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'active': False,
}