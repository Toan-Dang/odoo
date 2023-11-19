# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import xmlrpc.client
import json
from urllib.parse import urlparse


class Feedback(http.Controller):
    @http.route('/feedback/feedback', auth='public')
    def index(self, **kw):
        return "Hello, world"
    @http.route('/feedback/create', auth='user', type='json', methods=['POST'])
    def create_feedback_record(self, **kwargs):
        # Create a new record in the 'feedback' model
        print("kwargs", kwargs)
        print( "customer_name", kwargs['customer_name'])
        feedback_data = {
            "customer_name": kwargs['customer_name'],
            "customer_phone": kwargs['customer_phone'],
            "order_date": kwargs['order_date'],
            "order_id": kwargs['order_id'],
            "fb_rate": kwargs['fb_rate'],
            "fb_status": kwargs['fb_status'],
            "fb_comment": kwargs['fb_comment'],
            "fb_recomment": kwargs['fb_recomment'],
        }
        newFeedback = request.env['feedback'].create(feedback_data)
        return {'success': True, 'data': newFeedback.id }

    @http.route('/feedback/list',auth='user', type='json') 
    def getList(self):
        feedback_rec = request.env['feedback'].search([])
        feedback = []
        for rec in feedback_rec:
            vals = {
                "id": rec.id,
                "customer_name": rec.customer_name,
                "fb_rate": rec.fb_rate,
            }
            feedback.append(vals)
        print("list", feedback)
        return {'status': 200, 'response': feedback, 'message': 'success'}
#     @http.route('/feedback/feedback/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('feedback.listing', {
#             'root': '/feedback/feedback',
#             'objects': http.request.env['feedback.feedback'].search([]),
#         })

#     @http.route('/feedback/feedback/objects/<model("feedback.feedback"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feedback.object', {
#             'object': obj
#         })

