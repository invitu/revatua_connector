# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


class UniteMesureDouane(models.Model):
    _name = 'unite.mesure.douane'
    _description = "La liste des unités de mésure douanières"

    id_revatua = fields.Integer(string='ID')
    code = fields.Char(string='Libelle')
    libelle = fields.Char(string='Libelle')


class Variation(models.Model):
    _name='variation'
    _description='La variation'

    name = fields.Char(string='Nom de la variation')  # uniquement pour Odoo
    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID', help='Identifiant technique de la capacité')
    date_debut = fields.Date(string='Date début', help='La date de début')
    date_fin = fields.Date(string='Date fin', help='La date de fin')


class NomenclatureDouane(models.Model):
    _name='nomenclature.douane'
    _description = "La liste des nomenclatures douanières"

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID', help='Identifiant unique')
    variation_id = fields.Many2one(comodel_name='variation', string='Variation')
    libelle = fields.Char(string='Libelle', help='Libelle de la nomenclature')
    unite_mesure_douane_id = fields.Many2one(comodel_name='unite.mesure.douane', string='Unite Mésure Douane')
    designations_ids = fields.Many2many(comodel_name='designation', string='Désigantions', help='Liste de désignations synonymes')
    categorie_matiere_dangereuse_id = fields.Many2one(comodel_name='categorie.matiere.dangereuse', string='Catégorie Matière Dangereuse')
