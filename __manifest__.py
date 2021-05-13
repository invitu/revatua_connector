# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Revatua Connector",

    'summary': '',
    'description': """
Ce module permet de se conneter à l'API de Revatua
""",
    'author': 'INVITU, Tymofii GLUKHOV, Cyril Vinh Tung ',
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
        'data/res.partner.xml',
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
}
