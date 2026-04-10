from odoo import models, fields

class EmploymentDetail(models.Model):
    _name = 'hr_mgmt.employment_detail'
    _description = 'Employment Detail'
    _inherit = ['mail.thread']

    employee_id = fields.Many2one('hr_mgmt.employee', string='Employee', required=True, ondelete='cascade')
    date_joined = fields.Date(string='Date Joined', required=True)
    contract_type = fields.Selection([
        ('permanent', 'Permanent'),
        ('contract', 'Contract'),
        ('intern', 'Intern'),
        ('part_time', 'Part Time'),
    ], string='Contract Type', required=True)
    end_date = fields.Date(string='Contract End Date')
    probation_end = fields.Date(string='Probation End Date')
    salary = fields.Float(string='Basic Salary')
    bank_account = fields.Char(string='Bank Account')
    active = fields.Boolean(default=True)
