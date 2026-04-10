from odoo import models, fields

class Department(models.Model):
    _name = 'hr_mgmt.department'
    _description = 'Department'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Department Name', required=True, tracking=True)
    code = fields.Char(string='Code')
    manager_id = fields.Many2one('hr_mgmt.employee', string='Manager')
    parent_id = fields.Many2one('hr_mgmt.department', string='Parent Department')
    active = fields.Boolean(default=True)
    notes = fields.Text(string='Notes')
