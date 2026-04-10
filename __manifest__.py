{
    'name': 'HR Management System',
    'version': '18.0.1.0.0',
    'summary': 'Complete HR Management Module for Odoo 18',
    'description': """
        A full-featured Human Resources Management module covering:
        - Employee lifecycle management
        - Organisational structure
        - Time and attendance tracking
        - Leave management
        - Payroll processing
        - Recruitment and onboarding
        - Performance reviews
        - Document and compliance tracking
    """,
    'author': 'Muller Miles',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/sequence.xml',
        'views/department_views.xml',
        'views/designation_views.xml',
        'views/work_location_views.xml',
        'views/employee_views.xml',
        'views/employment_detail_views.xml',
        'views/attendance_views.xml',
        'views/leave_views.xml',
        'views/payroll_views.xml',
        'views/recruitment_views.xml',
        'views/performance_views.xml',
        'views/document_views.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
