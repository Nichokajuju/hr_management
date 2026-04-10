from odoo import models, fields

class JobOpening(models.Model):
    _name = 'hr_mgmt.job_opening'
    _description = 'Job Opening'
    _inherit = ['mail.thread']

    name = fields.Char(string='Job Title', required=True)
    department_id = fields.Many2one('hr_mgmt.department', string='Department')
    designation_id = fields.Many2one('hr_mgmt.designation', string='Designation')
    vacancies = fields.Integer(string='Number of Vacancies', default=1)
    deadline = fields.Date(string='Application Deadline')
    description = fields.Html(string='Job Description')
    state = fields.Selection([
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='open', tracking=True)


class Candidate(models.Model):
    _name = 'hr_mgmt.candidate'
    _description = 'Candidate'
    _inherit = ['mail.thread']

    name = fields.Char(string='Candidate Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    job_opening_id = fields.Many2one('hr_mgmt.job_opening', string='Applied For')
    resume = fields.Binary(string='Resume')
    resume_filename = fields.Char(string='Resume Filename')
    state = fields.Selection([
        ('new', 'New'),
        ('screening', 'Screening'),
        ('interview', 'Interview'),
        ('offered', 'Offered'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ], string='Status', default='new', tracking=True)
    notes = fields.Text(string='Notes')


class OfferLetter(models.Model):
    _name = 'hr_mgmt.offer_letter'
    _description = 'Offer Letter'
    _inherit = ['mail.thread']

    candidate_id = fields.Many2one('hr_mgmt.candidate', string='Candidate', required=True)
    job_opening_id = fields.Many2one('hr_mgmt.job_opening', string='Position')
    offer_date = fields.Date(string='Offer Date')
    joining_date = fields.Date(string='Expected Joining Date')
    offered_salary = fields.Float(string='Offered Salary')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ], string='Status', default='draft', tracking=True)
    notes = fields.Html(string='Offer Details')
