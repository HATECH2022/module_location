from odoo import api, fields, models, _
from odoo import exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class GestionAvenant(models.Model):
    _name = "gestion.avenant"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Gestion d'Avenant"
    
    name = fields.Char(string="Nom d'Avenant")
    date_avenant = fields.Date(string="Date Avenant",  default=fields.Date.today())
    lot_num = fields.Many2one('gestion.logement',string='Numéro de LOT')