# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api
from datetime import datetime


class Trajet(models.Model):
    _name = 'trajet'
    _description = "Liste des périples constituant le voyage"

    name = fields.Char(string='Nom')
    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID Revatua', help='ID Unique de trajet')
    date_depart = fields.Datetime(string="Date/heure de départ")
    ile_depart_id = fields.Many2one(comodel_name='res.country.state', string='Ile de départ')
    lieu_depart_id = fields.Many2one(comodel_name='res.partner', string='Lieu de départ')
    date_arrivee = fields.Datetime(string="Date/heure d'arivée")
    ile_arrivee_id = fields.Many2one(comodel_name='res.country.state', string="Ile d'arivée")
    lieu_arrivee_id = fields.Many2one(comodel_name='res.partner', string="Lieu d'arivée")
    voyage_id = fields.Many2one(comodel_name='voyage', string='Voyage',
                                )
    manifestes_ids = fields.Many2many(comodel_name='manifeste', string='Manifestes')
    generer_manifeste = fields.Boolean(string='Générer manifeste')
    date_derniere_modification_connaissement = fields.Datetime(string='Date de la derniere  modification de connaissement')

    @api.onchange('ile_depart_id')
    def ile_depart_id_change(self):
        if not self.ile_depart_id:
            return
        self.name = self.ile_depart_id.name


class Navire(models.Model):
    _name = 'navire'
    _description = 'Navire concerné'

    name = fields.Char(string='Nom', help='Nom du navire')
    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID Revatua', help='Identifiant technique unique du navire')
    abbreviation = fields.Char(string='Abbréviation', help='Abbréviation du nom du navire')
    vehicule_roulant = fields.Boolean(string='Embarquement de voitures', help="Accepte l'embarquement de véhicules")
    armateur_id = fields.Many2one(comodel_name='armateur', string='Armateur')
    licences_ids = fields.Many2many(comodel_name='licence', string='Licences', help='Licences du navire')
    croisiere = fields.Boolean(string='Croisière', help='Le navire est-il un navire de croisière')


class Voyage(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = 'voyage'

    name = fields.Char('Numéro de voyage',
                       readonly=True,
                       copy=False,
                       help='Le numéro de voyage, identifiant unique')
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirmed'),
            ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, default='draft')
    version = fields.Char('Version', help="La version des données - pour gérer les problèmes de concurrence")
    navire_id = fields.Many2one(comodel_name='navire', string='Navire',
                                readonly=True,
                                states={
                                    'draft': [('readonly', False)],
                                    'confirm': [('readonly', False)],
                                },
                                )
    date_depart = fields.Datetime(string='Date de depart',
                                  readonly=True,
                                  states={
                                      'draft': [('readonly', False)],
                                      'confirm': [('readonly', False)],
                                  },
                                  help='Date de départ du premier trajet du voyage')
    ile_depart_id = fields.Many2one(comodel_name='res.country.state', string='Ile de départ',
                                    readonly=True,
                                    states={
                                        'draft': [('readonly', False)],
                                        'confirm': [('readonly', False)],
                                    },
                                    )
    lieu_debarquement_depart_id = fields.Many2one(
        comodel_name='res.partner', string='Lieu de debarquement pour le départ',
        readonly=True,
        states={
            'draft': [('readonly', False)],
            'confirm': [('readonly', False)],
        },
    )
    date_arrivee = fields.Datetime(string="Date d'arivée",
                                   readonly=True,
                                   states={
                                       'draft': [('readonly', False)],
                                       'confirm': [('readonly', False)],
                                   },
                                   help="Date d'arrivée du dernier trajet du voyage")
    ile_arrivee_id = fields.Many2one(comodel_name='res.country.state', string="Ile d'arrivee",
                                     readonly=True,
                                     states={
                                         'draft': [('readonly', False)],
                                         'confirm': [('readonly', False)],
                                     },
                                     )
    lieu_debarquement_arrivee_id = fields.Many2one(
        comodel_name='res.partner', string="Lieu de debarquement pour l'arivée",
        readonly=True,
        states={
            'draft': [('readonly', False)],
            'confirm': [('readonly', False)],
        },
    )
    numero_armateur = fields.Char(string='Numéro Armateur', help="Numérotation du voyage propre à l'armateur")
    date_edition_avis_depart = fields.Date(string="Date d'édition de l'avis de départ")
    armateur_id = fields.Many2one(comodel_name='armateur', string='Armateur')
    annule = fields.Boolean(string='Annulé', help="L'indicateur d'annulation")
    trajet_ids = fields.One2many(
        comodel_name='trajet', inverse_name='voyage_id', string='Trajets',
        readonly=True,
        states={
            'draft': [('readonly', False)],
            'confirm': [('readonly', False)],
        },
    )
    date_dernier_maj = fields.Datetime(string='Date de MAJ')

    def _get_periple(self):
        periple = []
        for line in self.trajet_ids:
            periple.append({
                "dateDepart": line.date_depart.strftime("%Y-%m-%d"),
                "heureDepart": line.date_depart.strftime("%H:%M"),
                "idIleDepart": line.ile_depart_id.id_revatua,
                "idlieudepart": line.lieu_depart_id.id_revatua,
                "dateArrivee": line.date_arrivee.strftime("%Y-%m-%d"),
                "idIleArrivee": line.ile_arrivee_id.id_revatua,
                "heureArrivee": line.date_arrivee.strftime("%H:%M"),
                "idlieuarrivee":  line.lieu_arrivee_id.id_revatua
            })
        return periple

    def action_confirm(self):
        for voyage in self:
            if not voyage.name:
                periple = voyage._get_periple()
                payload = {
                    "idNavire": voyage.navire_id.id_revatua,
                    "periple": periple,
                }
                voyage_response = voyage.env['revatua.api'].api_post("voyages", payload)
                voyage.name = voyage_response.json()["numero"]
                voyage.version = voyage_response.json()["version"]
                voyage.date_depart = datetime.combine(
                    datetime.strptime(voyage_response.json()["dateDepart"], '%Y-%m-%d'),
                    datetime.strptime(voyage_response.json()["heureDepart"], '%H:%M:%S').time(),
                )
            else:
                payload = {
                    "annule": False,
                }
                url = 'voyages/' + voyage.name
                voyage_response = voyage.env['revatua.api'].api_put(url, payload)
            voyage.state = 'confirm'

    def action_cancel(self):
        if self.name:
            url = 'voyages/' + self.name
            voyage_response = self.env['revatua.api'].api_patch(url)
        self.state = 'cancel'

    def write(self, values):
        res = super(Voyage, self).write(values)
        if self.name and values.get('trajet_ids'):
            periple = self._get_periple()
            version = self.version
            payload = {
                "idNavire": self.navire_id.id_revatua,
                "periple": periple,
                "version": version,
            }
            print(payload)
            url = 'voyages/' + self.name
            voyage_response = self.env['revatua.api'].api_put(url, payload)
            self.version = voyage_response.json()["version"]
            self.date_depart = datetime.combine(
                datetime.strptime(voyage_response.json()["dateDepart"], '%Y-%m-%d'),
                datetime.strptime(voyage_response.json()["heureDepart"], '%H:%M:%S').time(),
            )
        return res


class TrajetTemporaire(models.Model):
    _name = 'trajet.temporaire'
    _description = "Liste des périples constituant le voyage"

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID', help='ID Unique de trajet')
    date_depart = fields.Datetime(string="Date/heure d'arivée")
    ile_depart_id = fields.Many2one(comodel_name='res.country.state', string='Ile de départ')
    lieu_depart_id = fields.Many2one(comodel_name='res.partner', string='Lieu de départ')
    date_arrivee = fields.Datetime(string="Date/heure d'arivée")
    ile_arrivee_id = fields.Many2one(comodel_name='res.country.state', string="Ile d'arivée")
    lieu_arrivee_id = fields.Many2one(comodel_name='res.partner', string="Lieu de l'arivée")


class VoyageTemporaire(models.Model):
    _name = 'voyage.temporaire'

    version = fields.Char(string='Version', help="La version des données - pour gérer les problèmes de concurrence")
    numero = fields.Char(string='Numéro de voyage', help='Le numéro de voyage, identifiant unique')
    navire_id = fields.Many2one(comodel_name='navire', string='Navire')
    date_depart = fields.Datetime(string='Date de depart', help='Date de départ du premier trajet du voyage')
    ile_depart_id = fields.Many2one(comodel_name='res.country.state', string='Ile de départ')
    lieu_debarquement_depart_id = fields.Many2one(comodel_name='res.partner', string='Lieu de debarquement pour le départ')
    date_arrivee = fields.Datetime(string="Date d'arivée", help="Date d'arrivée du dernier trajet du voyage")
    ile_arrivee_id = fields.Many2one(comodel_name='res.country.state', string="Ile d'arrivee")
    lieu_debarquement_arrivee_id = fields.Many2one(comodel_name='res.partner')
    periple_ids = fields.Many2many(comodel_name='trajet.temporaire', string='Periples')
    anomalies = fields.Char(string='La liste des anomalies')
