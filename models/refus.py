# -*- coding: utf-8 -*-
# part of odoo. see license file for full copyright and licensing details.
from odoo import fields, models


class MotifRefus(models.Model):
    _name = 'motif.refus'
    _description = "La liste des motifs de refus"

    version = fields.Datetime(string='Version')
    id_revatua = fields.Integer(string='ID')
    libelle = fields.Char(string='Motif', help='Libelle de motif. Ex: Plus de place sur le navire')
    commentaire_obligatoire = fields.Boolean(string='Commentaire?', help='le commentaire est-il obligatoire?')
