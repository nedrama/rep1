from odoo import models, fields


class Worker(models.Model):
    _name = "worker"

    name = fields.Char('Vardas')
    works = fields.Many2many("info_storage.book", relation="worker_rel",string='Atsakingi už')
