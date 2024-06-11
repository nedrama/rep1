from . import models
from . import controllers
from . import wizard
from odoo import api, fields, tools
def add_workers(cr, registry):
    tools.convert_file(cr, 'info_storage', './data/worker.csv', None, mode='init', noupdate=True, kind='init', report=None)