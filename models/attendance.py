from odoo import models, fields

class Attendance(models.Model):
    _name = 'hr_mgmt.attendance'
    _description = 'Attendance'

    employee_id = fields.Many2one('hr_mgmt.employee', string='Employee', required=True)
    date = fields.Date(string='Date', required=True)
    check_in = fields.Datetime(string='Check In')
    check_out = fields.Datetime(string='Check Out')
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('half_day', 'Half Day'),
    ], string='Status', default='present')
    notes = fields.Text(string='Notes')
