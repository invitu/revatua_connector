# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


class Autorisation(models.Model):
    _name = 'autorisation'
    _description = 'Liste des îles autorisées par la licence'
# pas besoin de name, il y a la reference
    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID')
    date_debut = fields.Date(string='Date de début', help="Date de début de l'autorisation")
    date_fin = fields.Date(string='Date de fin', help="Date de fin de l'autorisation")
    exceptionnel = fields.Boolean(string='Exceptionnel', help='Est-ce une autorisation exceptionnelle')
    ile_id = fields.Many2one(comodel_name='res.country.state', string='Ile')
    reference = fields.Char(string='Référence')
    commentaire = fields.Text(string='Commentaire', help="Commentaire dans le cas d'une autorisation exceptionnelle")
