# -*- coding: utf-8 -*-

from odoo import models, fields


class feedback(models.Model):
    _name = 'feedback'
    _description = 'feedback addons'

    customer_name = fields.Char()
    customer_phone = fields.Char()
    order_date = fields.Date()
    order_id = fields.Char()
    fb_rate = fields.Integer()
    fb_status = fields.Boolean()
    fb_comment = fields.Text()
    fb_recomment = fields.Selection([('yes', 'Yes'), ('no', 'No'), ('other', 'Others')], default='yes')
