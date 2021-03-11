# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


class CodeAvantage(models.Model):
    _name = 'code.avantage'
    _description = 'La liste des codes avantage'

    version = fields.Datetime(string='Version')
    code = fields.Char(string='Code Avantage', help='Code Avantage : Identifiant')
    libelle = fields.Char(string='Libellé', help='Le libellé du code avantage')
