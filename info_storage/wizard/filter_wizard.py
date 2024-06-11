from odoo import models, fields, http

class filter_wizard(models.TransientModel):
    _name='filter.wizard'

    worker = fields.Many2one('worker', string='Darboutojas')
    from_date = fields.Date('Nuo')
    to_date = fields.Date('Iki')
        

    def filter_books(self):
        
        tree_view_id = self.env.ref('info_storage.view_tree_book').ids
        form_view_id = self.env.ref('info_storage.view_form_book').ids
        return {
            'name': 'Filtruoti',
            'view_mode': 'tree',
            'views': [[tree_view_id, 'tree'], [form_view_id, 'form']],
            'res_model': 'info_storage.book',
            'type': 'ir.actions.act_window',
            'domain': [('cdate', '>=', self.from_date), ('cdate', '<=', self.to_date), ('worker.id', '=', self.worker.id)],
        }
