```python
from odoo import models, fields

class SavedPCBuilds(models.Model):
    _name = 'custom_pc_builder.saved_pc_builds'
    _description = 'Saved PC Builds'

    user_id = fields.Many2one('res.users', string='User', required=True)
    build_id = fields.Many2one('custom_pc_builder.pc_builds', string='PC Build', required=True)
    saved_at = fields.Datetime(string='Saved At', default=fields.Datetime.now, required=True)
```