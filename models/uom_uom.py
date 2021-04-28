# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _


class UoM(models.Model):
    _inherit = 'uom.uom'

    code_revatua = fields.Char(string='Code Revatua', size=64)
