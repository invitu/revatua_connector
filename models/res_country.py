# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class CountryState(models.Model):
    _inherit = 'res.country.state'

    id_revatua = fields.Integer(string='id', help="Identifiant unique de l'ile. Nombre entier")
    privee = fields.Boolean(string='Privée', help="L'île est-elle privée ? faux par défaut")
    code_zone_tarifaire = fields.Char(string='Code Zone Tarifaire', help="Le code de la zone tarifaire auquel l'île est rattachée")
    version = fields.Datetime(string='Version', help="Version de l'objet. C'est date/heure")
    ordre_desserte = fields.Integer(string='Ordre de desserte', help="Ordre de desserte de l'ile. Informatif")
    lieuDebarquements_ids = fields.Many2many(comodel_name='res.partner', string="Lieux d'embarquement-débarquement", help="Liste de lieux d'embarquement-débarquement")
