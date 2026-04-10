from odoo import models, fields

class WorkLocation(models.Model):
    _name = 'hr_mgmt.work_location'
    _description = 'Work Location'

    name = fields.Char(string='Location Name', required=True)
    address = fields.Text(string='Address')
    active = fields.Boolean(default=True)
