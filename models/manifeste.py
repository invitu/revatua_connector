# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class Manifeste(models.Model):
    _name = 'manifeste'
    _description = "La liste de manifestes pour les trajets et voyages"

#  pas besoin de name, il y a  le nom de fichier...   Peut etre on a meme pas besoin de l'objet
    id_revatua = fields.Integer(string='ID Manideste')  # id
    version = fields.Datetime(string='Version')
    date_edition = fields.Datetime(string='Date Edition')
    revatua_type = fields.Char(string='Type')
    nom_fichier = fields.Char(string='Nom de Fichier')
    pdf_connaissements = fields.Char(string='Connaissements PDF')
    signe = fields.Boolean(string='Signe')


class CumulChargementManifeste(models.Model):
    _name = 'cumul.chargement.manifeste'
    _description = "Calcul les cumuls des connaissements pour le manifeste entrée ou sortie"

    quantite_poids_embarque = fields.Float(string='Quantité de poids embarqué', digits=(16, 3), help='Le poids embarqué')
    unite_mesure_poids = fields.Char(string='UM Poids', help="L'unité de mesure du poids")
    quantite_volume_embarque = fields.Float(string='Quantité de poids embarqué', digits=(16, 3), help='Le poids embarqué')
    unite_mesure_volume = fields.Char(string='UM Volume', help="L'unité de mesure du volume")

    valeur_declaree = fields.Integer(string='Valeur Déclarée', help='La valeur totale déclarée')
    nb_colis = fields.Integer(string='Nb Colis', help='Le nombre de colis')


class EnteteManifeste(models.Model):
    _name = 'entete.manifeste'
    _description = "Les données de l'entete de manifestes"

    name = fields.Char(string="Nom de l'entête")  # uniquement pour Odoo
    type_revatua = fields.Char(string='Type', help='Help note')
    type_revatua = fields.Selection(selection=[
        ('SORTIE', 'Sortie'),
        ('ENTREE', 'Entrée')], string='Type')
    libelle_navire = fields.Char(string='Libelle Navire')
    numero_voyage = fields.Char(string='Numéro Voyage')
    date_voyage = fields.Datetime(string='Date/heure de voyage')
    nb_passagers = fields.Integer(string='Nombre de passagers')
    tonnage = fields.Float(string='Tonnage', digits=(16, 3))
    volume = fields.Float(string='Volume', digits=(16, 3))
    archipels = fields.Char(string='Archipels')
    iles_ids = fields.Many2many(comodel_name='res.country.state', string='Iles')
    nb_colis = fields.Integer(string='Nb Colis')  # One2One???
    valeur_declaree = fields.Integer(string='Valeur Déclarée', help='La valeur totale déclarée')  #One2one???
    date_edition = fields.Datetime(string="Date d'édition")
    cumul_matiere_dangereuse_ids = fields.Many2many(comodel_name='cumul.matiere.dangereuse', string='Cumul Matière Dangereuse')
    nom_utilisateur = fields.Char(string="Nom d'utilisateur")
