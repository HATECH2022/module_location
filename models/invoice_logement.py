from odoo import api, fields, models, _
from _datetime import date
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class LogementInvoice(models.Model):
    _name = 'account.mkove'
    _rec_name = 'lot'
    _inherit = 'sale.order'

    lot = fields.Many2one('gestion.parcelle', 'N° LOT de logement')