```python
from odoo import models, fields

class PCComponents(models.Model):
    _name = 'pc.components'
    _description = 'PC Components'

    component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('ram', 'RAM'),
        ('gpu', 'GPU'),
        ('storage', 'Storage'),
        ('peripherals', 'Peripherals'),
    ], string='Component Type', required=True)

    component_name = fields.Char(string='Component Name', required=True)
    component_specifications = fields.Text(string='Component Specifications')
```