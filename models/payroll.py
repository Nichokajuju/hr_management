from odoo import models, fields, api

class SalaryStructure(models.Model):
    _name = 'hr_mgmt.salary_structure'
    _description = 'Salary Structure'

    name = fields.Char(string='Structure Name', required=True)
    basic_salary = fields.Float(string='Basic Salary')
    housing_allowance = fields.Float(string='Housing Allowance')
    transport_allowance = fields.Float(string='Transport Allowance')
    other_allowances = fields.Float(string='Other Allowances')
    tax_deduction = fields.Float(string='Tax Deduction')
    other_deductions = fields.Float(string='Other Deductions')
    active = fields.Boolean(default=True)


class PaySlip(models.Model):
    _name = 'hr_mgmt.payslip'
    _description = 'Pay Slip'
    _inherit = ['mail.thread']

    employee_id = fields.Many2one('hr_mgmt.employee', string='Employee', required=True)
    salary_structure_id = fields.Many2one('hr_mgmt.salary_structure', string='Salary Structure')
    month = fields.Selection([
        ('01', 'January'), ('02', 'February'), ('03', 'March'),
        ('04', 'April'), ('05', 'May'), ('06', 'June'),
        ('07', 'July'), ('08', 'August'), ('09', 'September'),
        ('10', 'October'), ('11', 'November'), ('12', 'December'),
    ], string='Month', required=True)
    year = fields.Integer(string='Year', required=True)
    gross_salary = fields.Float(string='Gross Salary', compute='_compute_salary', store=True)
    total_deductions = fields.Float(string='Total Deductions', compute='_compute_salary', store=True)
    net_salary = fields.Float(string='Net Salary', compute='_compute_salary', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
    ], string='Status', default='draft', tracking=True)
    notes = fields.Text(string='Notes')

    @api.depends('salary_structure_id')
    def _compute_salary(self):
        for rec in self:
            if rec.salary_structure_id:
                s = rec.salary_structure_id
                gross = s.basic_salary + s.housing_allowance + s.transport_allowance + s.other_allowances
                deductions = s.tax_deduction + s.other_deductions
                rec.gross_salary = gross
                rec.total_deductions = deductions
                rec.net_salary = gross - deductions
            else:
                rec.gross_salary = 0
                rec.total_deductions = 0
                rec.net_salary = 0
