from odoo import models, fields

class Designation(models.Model):
    _name = 'hr_mgmt.designation'
    _description = 'Designation / Job Title'

    name = fields.Char(string='Designation', required=True)
    department_id = fields.Many2one('hr_mgmt.department', string='Department')
    active = fields.Boolean(default=True)
