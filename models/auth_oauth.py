
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AuthOAuthProvider(models.Model):
    """Class defining the configuration values of an OAuth2 provider"""
    _inherit = 'auth.oauth.provider'

    client_secret = fields.Char(string='Client Secret')
    response_type = fields.Selection([
        ('token', 'Token'), ('code', 'Code')
    ], default='token', required=True)
