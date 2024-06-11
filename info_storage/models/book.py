from odoo import models, fields

class Book(models.Model):
    _name = "info_storage.book"

    name = fields.Char("Pavadinimas", required=True)
    description = fields.Html("Aprašymas")
    company = fields.Char("Įmonė")
    maker = fields.Many2one('res.users','Kūrėjas', default=lambda self: self.env.user)
    worker = fields.Many2many("worker", relation="worker_rel", string="Atsakingi darbuotojai")
    cdate=fields.Date(string="Data", default=lambda s: fields.Date.context_today(s))

