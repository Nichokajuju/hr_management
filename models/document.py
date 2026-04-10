from odoo import models, fields

class EmployeeDocument(models.Model):
    _name = 'hr_mgmt.employee_document'
    _description = 'Employee Document'

    employee_id = fields.Many2one('hr_mgmt.employee', string='Employee', required=True, ondelete='cascade')
    name = fields.Char(string='Document Name', required=True)
    document_type = fields.Selection([
        ('id', 'National ID'),
        ('passport', 'Passport'),
        ('contract', 'Contract'),
        ('certificate', 'Certificate'),
        ('other', 'Other'),
    ], string='Document Type')
    file = fields.Binary(string='File')
    filename = fields.Char(string='Filename')
    expiry_date = fields.Date(string='Expiry Date')
    notes = fields.Text(string='Notes')


class DisciplinaryRecord(models.Model):
    _name = 'hr_mgmt.disciplinary_record'
    _description = 'Disciplinary Record'
    _inherit = ['mail.thread']

    employee_id = fields.Many2one('hr_mgmt.employee', string='Employee', required=True)
    date = fields.Date(string='Date', required=True)
    incident_type = fields.Selection([
        ('warning', 'Warning'),
        ('suspension', 'Suspension'),
        ('termination', 'Termination'),
        ('other', 'Other'),
    ], string='Incident Type', required=True)
    description = fields.Text(string='Description')
    action_taken = fields.Text(string='Action Taken')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('closed', 'Closed'),
    ], string='Status', default='draft', tracking=True)
