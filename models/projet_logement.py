import datetime
import requests
import json
import os
from requests.auth import HTTPBasicAuth
from odoo import api, fields, models, _
from odoo import exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class ProjetLogement(models.Model):
    _name = "projet.logement"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Projet de Logement"

    name = fields.Char(string="Nom du Projet")
    description = fields.Text(string="Description")

    _sql_constraints = [('projet_parcelle_uniq', 'unique(name)', 'Le nom du projet doit être unique !')]

