# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


class PrestationComplementaire(models.Model):
    _name = 'prestation.complementaire'
    _description = "La liste des prestations complémentaires"

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID', help="L'identifiant unique de la prestation")
    libelle = fields.Char(string='Libelle', help='Le libellé de la prestation')
    actif = fields.Boolean(string='Actif', help='Indique si la prestation est active ou pas')
