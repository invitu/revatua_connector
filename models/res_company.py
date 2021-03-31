# Part of Odoo. See LICENSE file for full copyright and licensing details.

import requests
from datetime import datetime as dt
from datetime import timedelta as td

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = 'res.company'

    revatua_endpoint = fields.Char(string='Validation URL', default="https://auth-revatua.auth.us-west-2.amazoncognito.com/oauth2/token")  # OAuth provider URL to validate tokens
    revatua_client_id = fields.Char(string='Client ID')  # Our identifier
    revatua_client_secret = fields.Char(string='Client Secret')
    revatua_oauth_access_token = fields.Char(string='OAuth Access Token', copy=False)
    revatua_token_expiry_date = fields.Datetime(string='Expiry Date')

    def get_token(self):
        data = {
            "grant_type": "client_credentials",
            "client_id": self.revatua_client_id,
            "client_secret": self.revatua_client_secret,
            "scope": "REVATUA/api.armateur"
        }
        try:
            r = requests.post(self.revatua_endpoint, data=data)
            if r.status_code != 200:
                raise UserError(_('We had trouble to create your data, retry later or contact your support if the problem persists - Error %s') % r.status_code)
            r.raise_for_status()
            self.revatua_token_expiry_date = dt.now() + td(seconds=r.json()["expires_in"])
            self.revatua_oauth_access_token = "Bearer " + r.json()["access_token"]
        except requests.exceptions.RequestException as e:
            _logger.exception(e)
            raise UserError(_('We had trouble to create your data, please retry later or contact your support if the problem persists - Network Error'))

    def check_validity(self):
        if self.revatua_token_expiry_date < dt.now():
            self.get_token()
