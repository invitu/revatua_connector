# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


class CategorieMatiereDangereuse(models.Model):
    _name = 'categorie.matiere.dangereuse'
    _description = "La liste des catégories de matières dangereuses"

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID')
    variation_id = fields.Many2one(comodel_name='variation', string='La variation')
    libelle = fields.Char(string='Libellé')
    codes_sh_parent = fields.Char(string='Codes SH Parent')


class CodeAvantage(models.Model):
    _name = 'code.avantage'
    _description = 'La liste de codes avantage'

    version = fields.Datetime(string='Version')
    code = fields.Char(string='Code Avantage', help='Code Avantage : Identifiant')
    libelle = fields.Char(string='Libellé', help='Le libellé du code avantage')


class DesignationBrouillon(models.Model):
    _name = 'designation.brouillon'
    _description = 'Liste de désignations synonymes'

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID')
    libelle = fields.Char(string='Libellé')
    code_avantage_id = fields.Many2one(comodel_name='code.avantage', string='Code Avantage')


class NomenclatureBrouillon(models.Model):
    _name = 'nomenclature.brouillon'
    _description = "La liste des nomenclatures en brouillon"

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID', help='Identifiant unique')
    nomenclature = fields.Char(string='Nomenclature')
    libelle = fields.Char(string='Libellé', help='Libellé de la nomenclature')
    designations_brouillon_id = fields.Many2one(comodel_name='designation.brouillon', string='Designation Brouillon')
    cat_mat_danger_id = fields.Many2one(comodel_name='categorie.matiere.dangereuse', string='Catégorie Matière Dangereuse')
    modification = fields.Integer(string='Modification')


class CumulMatiereDangereuse(models.Model):
    _name = 'cumul.matiere.dangereuse'
    _description = "Le poids total de la matière dangereuse"

    libelle = fields.Char(string='Libellé', help='Libellé de la nomenclature')
    quantite_poids_embarque = fields.Float(string='Quantité de poids embarqué', digits=(16, 3), help='Le poids embarqué')
    unite_mesure_poids = fields.Char(string='UM Poids', help="L'unité de mesure du poids")
