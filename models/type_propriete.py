import datetime
import requests
import json
import os
from requests.auth import HTTPBasicAuth
from odoo import api, fields, models, _
from odoo import exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class TypePropriete(models.Model):
    _name = "type.propriete"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Type de Propriete"

    name = fields.Char(string="Nom du Type")
    projetparcelle_id = fields.Many2one('projet.logement', 'Projet', required=True, tracking=True)
    description = fields.Text(string="Description")

    _sql_constraints = [('zone_parcelle_uniq', 'unique(name)', 'Le nom du zone lot doit être unique !')]


