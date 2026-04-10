from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class Employee(models.Model):
    _name = 'hr_mgmt.employee'
    _description = 'Employee'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Full Name', required=True, tracking=True)
    employee_id = fields.Char(string='Employee ID', copy=False, readonly=True, default='New')
    photo = fields.Image(string='Photo')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    national_id = fields.Char(string='National ID')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    department_id = fields.Many2one('hr_mgmt.department', string='Department', tracking=True)
    designation_id = fields.Many2one('hr_mgmt.designation', string='Designation', tracking=True)
    work_location_id = fields.Many2one('hr_mgmt.work_location', string='Work Location')
    manager_id = fields.Many2one('hr_mgmt.employee', string='Manager')
    employment_detail_ids = fields.One2many('hr_mgmt.employment_detail', 'employee_id', string='Employment Details')
    document_ids = fields.One2many('hr_mgmt.employee_document', 'employee_id', string='Documents')
    state = fields.Selection([
        ('active', 'Active'),
        ('on_leave', 'On Leave'),
        ('terminated', 'Terminated'),
    ], string='Status', default='active', tracking=True)
    active = fields.Boolean(default=True)
    notes = fields.Text(string='Notes')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age = relativedelta(fields.Date.today(), rec.date_of_birth).years
            else:
                rec.age = 0

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('employee_id', 'New') == 'New':
                vals['employee_id'] = self.env['ir.sequence'].next_by_code('hr_mgmt.employee') or 'New'
        return super().create(vals_list)
