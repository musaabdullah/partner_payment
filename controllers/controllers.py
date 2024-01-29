# -*- coding: utf-8 -*-
# from odoo import http


# class InvoicePayment(http.Controller):
#     @http.route('/invoice_payment/invoice_payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_payment/invoice_payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_payment.listing', {
#             'root': '/invoice_payment/invoice_payment',
#             'objects': http.request.env['invoice_payment.invoice_payment'].search([]),
#         })

#     @http.route('/invoice_payment/invoice_payment/objects/<model("invoice_payment.invoice_payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_payment.object', {
#             'object': obj
#         })
