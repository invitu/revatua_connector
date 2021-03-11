# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


# A VOIR SI ON DEPLACE CES CLASSES DANS TRAJET_VOYAGE.PY
class Passage(models.model):
    _name = 'passage'
    _description = "La liste de passages"

    name = fields.Char(string='Nom de passage')  # uniquement pour Odoo
    version = fields.Char(string='Version')
    id_revatua = fields.Integer(string='ID')
    date_depart = fields.Datetime(string='Date de depart', help='Date de départ du premier trajet du voyage')
#  verifier
    ile_depart_id = fields.Many2one(comodel_name='res.state', string='Ile de départ')
#  completer
    lieu_depart_id = fields.Many2one(comodel_name='res.partner', string='Lieu de debarquement pour le départ')
    date_arivee = fields.Datetime(string="Date d'arivée", help="Date d'arrivée du dernier trajet du voyage")
    ile_arivee_id = fields.Many2one(comodel_name='res.state', string="Ile d'arivee")
#   completer LieuDebarquement
    lieu_arivee_id = fields.Many2one(comodel_name='res.partner')

    nbre_adultes = fields.Integer(string='Nombre Adultes')
    nbre_jeunes = fields.Integer(string='Nombre Jeunes')
    nbre_seniors = fields.Integer(string='Nombre Seniors')
    nbre_scolaires = fields.Integer(string='Nombre Scolaires')
    nbre_croisieristes = fields.Integer(string='Nombre Croisieristes')
    nbre_abonnements = fields.Integer(string='Nombre Abonnements')
    nbre_voitures = fields.Integer(string='Nombre Voitures')
    nbre_velos = fields.Integer(string='Nombre Velos')
    nbre_motos = fields.Integer(string='Nombre Motos')
    nbre_utilitaires = fields.Integer(string='Nombre Utilitaires')
    nbre_camions = fields.Integer(string='Nombre Camions')


class EtatDePassage(models.model):
    _name = 'etat.passage'
    _description = "Les états de passages dans le voyage concerné"

    version = fields.Char(string='Version')
    id_revatua = fields.Integer(string='ID')
    voyage_id = fields.Many2one(comodel_name='voyage', string='Voyage')
    transmis = fields.Boolean(string='Transmis')
    passages_ids = fields.Many2many(comodel_name='passage', string='Passages')
