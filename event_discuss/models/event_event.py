# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, _


class EventEvent(models.Model):
    _inherit = 'event.event'

    def event_user_subscribe(self):
        pass
