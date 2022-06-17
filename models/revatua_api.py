# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import requests

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


REVATUA_BASE_URL = 'https://test.revatua.gov.pf/api/v1/'


class RevatuaApi(models.Model):
    _name = "revatua.api"
    _description = "Revatua Service"

    def get_headers(self):
        company = self.env.company
        company.check_validity()
        token = company.revatua_oauth_access_token
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "accept": "application/json",
        }
        return headers

    def api_post(self, url, data):
        url_request = REVATUA_BASE_URL + url
        headers = self.get_headers()
        try:
            r = requests.post(url_request, json=data, verify=False, headers=headers)
            if r.status_code == 500:
                raise UserError(_('Erreur Revatua Internal Server Error 500 sur %s : Contactez la DPAM !') % (url_request))
            elif r.status_code != 201:
                raise UserError(_('Message Revatua %s - Detail %s - Error %s sur %s : Contactez la DPAM !') % (r.json().get('message'), r.json().get('detail'), r.status_code, url_request))
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            _logger.exception(e)
            raise UserError(_('We had trouble to create your data, please retry later or contact your support if the problem persists - Network Error sur %s') % (url_request))
        return r

    def api_put(self, url, data):
        url_request = REVATUA_BASE_URL + url
        headers = self.get_headers()
        try:
            r = requests.put(url_request, json=data, verify=False, headers=headers)
            if r.status_code == 500:
                raise UserError(_('Erreur Revatua Internal Server Error 500 sur %s : Contactez la DPAM !') % (url_request))
            elif r.status_code != 200:
                raise UserError(_('Message Revatua %s - Detail %s - Error %s sur %s : Contactez la DPAM !') % (r.json().get('message'), r.json().get('detail'), r.status_code, url_request))
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            _logger.exception(e)
            raise UserError(_('We had trouble to create your data, please retry later or contact your support if the problem persists - Network Error sur %s') % (url_request))
        return r

    def api_patch(self, url, data):
        url_request = REVATUA_BASE_URL + url
        headers = self.get_headers()
        try:
            r = requests.patch(url_request, json=data, verify=False, headers=headers)
            if r.status_code == 500:
                raise UserError(_('Erreur Revatua Internal Server Error 500 sur %s : Contactez la DPAM !') % (url_request))
            elif r.status_code != 200:
                raise UserError(_('Message Revatua %s - Detail %s - Error %s sur %s : Contactez la DPAM !') % (r.json().get('message'), r.json().get('detail'), r.status_code, url_request))
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            _logger.exception(e)
            raise UserError(_('We had trouble to create your data, please retry later or contact your support if the problem persists - Network Error sur %s') % (url_request))
        return r

    def api_get(self, url):
        url_request = REVATUA_BASE_URL + url
        headers = self.get_headers()
        try:
            r = requests.get(url_request, verify=False, headers=headers)
            if r.status_code == 500:
                raise UserError(_('Erreur Revatua Internal Server Error 500 sur %s : Contactez la DPAM !') % (url_request))
            elif r.status_code != 200:
                raise UserError(_('Message Revatua %s - Detail %s - Error %s sur %s : Contactez la DPAM !') % (r.json().get('message'), r.json().get('detail'), r.status_code, url_request))
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            _logger.exception(e)
            raise UserError(_('We had trouble to create your data, please retry later or contact your support if the problem persists - Network Error sur %s') % (url_request))
        return r
