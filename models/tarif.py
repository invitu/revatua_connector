# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class UnitePayante(models.Model):
    _name = "unite.payante"
    _description = "La liste des unités de mesures payantes"

#  LIER AVEC  UOM?
    version = fields.Datetime(string='Version')
    code = fields.Char(string='Code', help="Code de l'unite payante - unique")
    libelle = fields.Char(string='Libellé')
    mesure = fields.Char(string='Unité de mesure')


class CodeTarif(models.Model):
    _name = 'code.tarif'
    _description = "Le code du tarif"

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='Tarif ID', help='Identifiant technique')
    code = fields.Char(string="Code d'idendification")
    libelle = fields.Char(string='Libellé', help='Libellé du code tarif')
    refrigere = fields.Boolean(string='Réfrigéré', help='Indique si le code tarif concerne du réfrigéré')
    obsolete = fields.Boolean(string='Obsolète', help='Indique si le code tarif est obsolète')
    unite_payantes_id = fields.Many2one(comodel_name='unite.payante', string='Unités payantes')


class DetailTarif(models.Model):
    _name = 'detail.tarif'
    _description = "Détails du tarif par tronçon"

    name = fields.Char(string='Nom de détail tarif')  #uniquement pour ODOO
    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='Detail ID', help='Identifiant unique du détail du tarif')
    ile_depart_id = fields.Many2one(comodel_name='res.country.state', string='Ile de départ')
    ile_arivee_id = fields.Many2one(comodel_name='res.country.state', string="Ile d'arrivée")
    code_tarif_id = fields.Many2one(comodel_name='code.tarif', string='Code Tarif')
    montant = fields.Float(string='Montant', digits=(16, 2), help='Montant maximum de fret')


class Tarif(models.Model):
    _name = 'tarif'
    _description = "La liste de tarifs"

    name = fields.Char(string='Nom de Tarif')  # uniquement pour ODOO
    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='Tarif ID', help='Identifiant du tarif')
    date_application = fields.Date(string="Date d'application", help="Date à partir de laquelle le tarif s'applique")
    date_fin = fields.Date(string="Date de fin", help="Date de fin de validité du tarif")
    reference = fields.Char(string='Référence', help='Texte de référénce')
    tarif_minimum = fields.Integer(string='Min tarif', help='Tarif minimum pour un connaissement')
    tarif_tuam_10 = fields.Integer(string='Tarif inter Tuamotu', help="Tarif inter île Tuamotu jusqu'à 10 miles")
    tarif_tuam_sup = fields.Integer(string='Tarif Sup inter Tuamotu', help='Tarif inter île Tuamotu par 10 miles de plus')


class JournalTraitementTarif(models.Model):
    _name = "journal.traitement.tarif"
    _description = "La liste de journaux des traitement tarifaires"

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID')
    tarif_id = fields.Many2one(comodel_name='tarif', string='Tarif')
    state = fields.Selection(selection=[
        ('ANOMALIE', 'Anomalie'),
        ('TERMINE', 'Terminé')], string='Etat')
    date_traitement = fields.Date(string='Date de traitement')
    nom_fichier = fields.Char(string='Nom de fichier')  # Pas besoin de name du coup
