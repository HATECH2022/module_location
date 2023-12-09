from odoo import api, fields, models, _
from odoo import exceptions
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class GestionLogement(models.Model):
    _name = "gestion.logement"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Gestion de Logement"
    _rec_name='lot'

    lot = fields.Char(string="N° LOT", size=32, required=True, tracking=True)
    client_id = fields.Many2one('res.partner', 'Propriétaire', tracking=True, size=32)
    accountmove_order_id = fields.Many2one('account.move', 'Facture', tracking=True, size=32)

    zoneparcelle_id = fields.Many2one('type.propriete', 'Type de Propriete',  tracking=True)
    projetparcelle_id = fields.Many2one('projet.logement', 'Projet', required=True, tracking=True)
    
    avenant_ids = fields.One2many('gestion.avenant', 'lot_num', string='Avenants',size=32, tracking=True)
    # avenant_nom = fields.One2many('gestion.avenant',   required=True, tracking=True)


    status = fields.Selection([
        ('cancelled', 'Annulé'),
        ('draft', 'Créé'),
        ('process', 'En Traitement'),
        ('invoiced', 'En Facturation'),
        ('paid', 'Vendu')
    ], 'Statut de Location', default='draft')

    type_location = fields.Selection([
        ('Location Vente', 'Location Vente'),
       ('Location Simple', 'Location Simple')], 'Etat de Location', default='', required=True, size=32 , tracking=True)

    surface = fields.Float(string="Surface (m2)",  tracking=True)
    
    
    decompte = fields.Boolean('Decompte')
    acte_de_vente= fields.Boolean('Acte de Vente')
    contrat = fields.Boolean('Contrat')

   

    date_affectation = fields.Date(string="Date Affectation",  default=fields.Date.today())
    date_fin_contrat = fields.Date(string="Date Fin du Contrat", default=fields.Date.today())

    dure_paiement = fields.Char(string="Dure (ans)", size=32, tracking=True)

    interet = fields.Float('Interet (ans)')

    prix_vente_comptent = fields.Integer(string="Prix Vente de Comptant", size=32, tracking=True)

    reliquat_apres_apport_personnel = fields.Integer(string="Reliquat Apres Apport Personnel", size=32, tracking=True)

    loyer_mensuelle = fields.Integer(string="Loyer Mensuelle", size=32, tracking=True)

    loyer_total = fields.Integer(string="Loyer Total", size=32, tracking=True)

    apport_personnel = fields.Integer(string="Apport Personnel", size=32, tracking=True)

    valeur_vente = fields.Integer(string="Valeur Vente (Fdj)", size=32, tracking=True)

    duree = fields.Char(string="Duree", size=32, tracking=True)

    nbr_echeance = fields.Integer(string="Nombre D'echeance", size=32, tracking=True)

    mode_paiement = fields.Selection([
        ('Virement de Banque', 'Virement de Banque'),
       ('Comptant', 'Comptant'), ('Tresorie National', 'Tresorie National')], 'Mode de Paiement', default='', required=True, size=32, tracking=True)


    def mettre_enlocation(self):
        print("******** change le status en location", self.status)
        if self.status != 'draft':
            if self.status == 'process':
                raise UserError(_('Cette location est en Traitement !!!'))
            if self.status == 'paid':
                raise UserError(_('Cette location est PAYER !!!'))
            if self.status == 'invoiced':
                raise UserError(_('Cette location est en Facturation !!!'))

            raise UserError(_('Cette location ne peut pas être LOUE !!!'))

        return self.update({"status": 'process'})