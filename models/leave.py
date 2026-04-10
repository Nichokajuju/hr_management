from odoo import models, fields

class LeaveType(models.Model):
    _name = 'hr_mgmt.leave_type'
    _description = 'Leave Type'

    name = fields.Char(string='Leave Type', required=True)
    max_days = fields.Integer(string='Max Days Per Year')
    active = fields.Boolean(default=True)


class LeavePolicy(models.Model):
    _name = 'hr_mgmt.leave_policy'
    _description = 'Leave Policy'

    name = fields.Char(string='Policy Name', required=True)
    leave_type_id = fields.Many2one('hr_mgmt.leave_type', string='Leave Type', required=True)
    allowed_days = fields.Integer(string='Allowed Days')
    active = fields.Boolean(default=True)


class LeaveRequest(models.Model):
    _name = 'hr_mgmt.leave_request'
    _description = 'Leave Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr_mgmt.employee', string='Employee', required=True)
    leave_type_id = fields.Many2one('hr_mgmt.leave_type', string='Leave Type', required=True)
    date_from = fields.Date(string='From Date', required=True)
    date_to = fields.Date(string='To Date', required=True)
    reason = fields.Text(string='Reason')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)
