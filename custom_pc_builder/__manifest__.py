{
    'name': 'Custom PC Builder',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Custom PC Building Module',
    'sequence': 1,
    'description': """
    Custom PC Building Module for Odoo 16 Community Edition
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'website_sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/component_selection_view.xml',
        'views/pc_build_preview_view.xml',
        'views/saved_pc_builds_view.xml',
        'reports/saved_pc_builds_report.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}