```python
from odoo import http
from odoo.http import request

class ComponentSelectionController(http.Controller):

    @http.route('/pc_builder/component_selection', type='http', auth='user', website=True)
    def component_selection(self, **kwargs):
        pc_components = request.env['pc.components'].sudo().search([])
        return request.render('custom_pc_builder.component_selection', {
            'pc_components': pc_components
        })

    @http.route('/pc_builder/update_build', type='json', auth='user')
    def update_build(self, component_id, **kwargs):
        component = request.env['pc.components'].sudo().browse(int(component_id))
        pc_build = request.env['pc.builds'].sudo().search([('user_id', '=', request.uid)], limit=1)
        if not pc_build:
            pc_build = request.env['pc.builds'].sudo().create({
                'user_id': request.uid,
                'component_ids': [(4, component.id)]
            })
        else:
            pc_build.write({
                'component_ids': [(4, component.id)]
            })
        return {
            'status': 'success',
            'message': 'PC build updated successfully.'
        }

    @http.route('/pc_builder/preview_build', type='http', auth='user', website=True)
    def preview_build(self, **kwargs):
        pc_build = request.env['pc.builds'].sudo().search([('user_id', '=', request.uid)], limit=1)
        return request.render('custom_pc_builder.pc_build_preview', {
            'pc_build': pc_build
        })
```