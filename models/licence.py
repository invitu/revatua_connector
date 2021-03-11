# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


class Licence(models.Model):
    _name = 'licence'
    _description = 'Licences du navire'

    name = fields.Char(string='Nom de licence')  # uniquement pour odoo
    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID')
    date_octroit = fields.Date(string='Date Octroit')
    date_fin = fields.Date(string='Date de fin', help="Date de fin de l'autorisation")
    reference = fields.Char(string='Référence')
    commentaire = fields.Text(string='Commentaire', help="Commentaire dans le cas d'une autorisation exceptionnelle")
    armateur_id = fields.Many2one(comodel_name='res.partner', string='Armateur')
    autorisations_ids = fields.Many2many(comodel_name='autorisation', string='Autorisations', help='Liste des autorisation')
    port_base_id = fields.Many2one(comodel_name='res.partner', string='Port de base ', help='Ex: Vairao')
