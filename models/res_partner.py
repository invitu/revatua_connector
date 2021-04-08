# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    id_revatua = fields.Integer(string='ID Revatua',)
