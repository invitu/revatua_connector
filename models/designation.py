# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Designation(models.Model):
    _name = 'designation'
    _description = "Récupération de la liste des désignations/nomenclatures par rapport a un critère."

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID')
    libelle = fields.Char(string='Libellé')
    code_avantage_id = fields.Many2one(comodel_name='code.avantage', string='Code Avantage')
