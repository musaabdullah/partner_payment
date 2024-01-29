
from odoo import api, models, fields, _

class PartnerPayment(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner Payment'


    payment_count = fields.Integer(compute='_payment_count',String="Payments")


    def _payment_count(self):
        for rec in self:
            document_ids = self.env['account.payment'].search([('partner_id', '=', rec.id)])
            rec.payment_count = len(document_ids)

    def action_view_payment(self): 
        self.ensure_one()
        ctx = dict(
            create=True,
        #    write=True,
            delete=False,
        )
        return {
            'type': 'ir.actions.act_window',
            'name': 'Payments',
            'view_mode': 'tree,form',
            'res_model': 'account.payment',
            'domain': [('partner_id', '=', self.id)],
            'context': ctx,
        }