# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


# pas sur que nous avons besoin de cet objet
class InfoComplementaireAvisDepart(models.Model):
    _name = 'info.complementaire.avis.depart'
    _description = "Les informations complèmentaires pour l'avis de depart"

    informations_complementaires = fields.Char(string='Infos Complementaires')
    envoyer_mail = fields.Boolean(string='Envoyer un mail', help="Envoyer l'avis de départ par mail aux destinataires institionnels", default=False)
