# Copyright 2021 INVITU - Cyril VINH-TUNG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Revatua Connector",

    'summary': '',
    'description': """
Ce module permet de se conneter à l'API de Revatua
""",
    'author': 'INVITU',
    'website': 'http://www.invitu.com',

    'category': 'API',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
        'l10n_pf_archipels',
    ],

    # always loaded
    'data': [
        'security/revatua_security.xml',
        'data/product_data.xml',
        'data/res_partner.xml',
        'data/uom_uom_data.xml',
        'data/res.country.state.csv',
        'data/product.template.csv',
        'views/uom_uom_views.xml',
        'views/revatua_menu_views.xml',
        'views/res_company_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'license': 'AGPL-3',
}
