# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Revatua Profile",

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
        'auth_oauth',
    ],

    # always loaded
    'data': [
        'views/auth_oauth_views.xml',
        'data/auth_oauth_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
}
