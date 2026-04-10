from odoo import models, fields

class Goal(models.Model):
    _name = 'hr_mgmt.goal'
    _description = 'Employee Goal'
    _inherit = ['mail.thread']

    name = fields.Char(string='Goal Title', required=True)
    employee_id = fields.Many2one('hr_mgmt.employee', string='Employee', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    progress = fields.Integer(string='Progress (%)', default=0)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('achieved', 'Achieved'),
        ('not_achieved', 'Not Achieved'),
    ], string='Status', default='draft', tracking=True)


class PerformanceReview(models.Model):
    _name = 'hr_mgmt.performance_review'
    _description = 'Performance Review'
    _inherit = ['mail.thread']

    employee_id = fields.Many2one('hr_mgmt.employee', string='Employee', required=True)
    reviewer_id = fields.Many2one('hr_mgmt.employee', string='Reviewer')
    review_date = fields.Date(string='Review Date', required=True)
    period = fields.Char(string='Review Period')
    rating = fields.Selection([
        ('1', 'Poor'),
        ('2', 'Below Average'),
        ('3', 'Average'),
        ('4', 'Good'),
        ('5', 'Excellent'),
    ], string='Rating')
    comments = fields.Text(string='Comments')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
    ], string='Status', default='draft', tracking=True)
