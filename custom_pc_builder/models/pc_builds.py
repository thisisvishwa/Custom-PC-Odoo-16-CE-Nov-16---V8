```python
from odoo import models, fields

class PcBuilds(models.Model):
    _name = 'pc.builds'
    _description = 'PC Builds'

    user_id = fields.Many2one('res.users', string='User', required=True)
    component_ids = fields.Many2many('pc.components', string='Components')
    build_config = fields.Text(string='Build Configuration')

    def preview_build(self):
        # Logic for previewing the build goes here
        pass

    def save_build(self):
        # Logic for saving the build goes here
        pass

    def share_build(self):
        # Logic for sharing the build goes here
        pass
```