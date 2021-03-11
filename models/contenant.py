# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


class Capacite(models.Model):
    _name = 'capacite'
    _description = "Les capacités de contenants possibles"

    name = fields.Char(string='Nom de capacité')  # uniquement pour Odoo, a-t-on réelement besoin??
    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID')
    quantite = fields.Float(string='Quantité', digits=(16, 3), help='La quantité')
    unite = fields.Selection(selection=[('LITRE', 'L'),
                                        ('M3', 'm3'),
                                        ('DM3', 'dm3')], string='Unité', help="L'unité de volume de la capacité")


class Contenant(models.Model):
    _name = 'contenant'
    _description = "La liste des contenants"

    version = fields.Char(string='Version')
    id_revatua = fields.Integer(string='ID', help='Identifiant technique du contenant')
    libelle = fields.Char(string='Libelle', help='Le libellé du contenant. Ex: BAC')
    capacites_ids = fields.Many2many(comodel_name='capacite', string='Capacités', help='Liste des capacités possibles')
