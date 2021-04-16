# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    est_contenant = fields.Boolean(string='Est un contenant',
                                   help='Cochez cette case si cet article est un contenant')
    id_revatua = fields.Integer(string='Id Revatua', help='Identifiant Revatua')
