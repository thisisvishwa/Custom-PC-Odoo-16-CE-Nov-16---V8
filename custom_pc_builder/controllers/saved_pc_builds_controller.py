```python
from odoo import http
from odoo.http import request

class SavedPCBuildsController(http.Controller):

    @http.route('/pc_builder/saved_builds', type='http', auth='user')
    def list_saved_builds(self, **kwargs):
        saved_builds = request.env['saved.pc.builds'].search([('user_id', '=', request.uid)])
        return request.render('custom_pc_builder.saved_builds', {'builds': saved_builds})

    @http.route('/pc_builder/save_build', type='json', auth='user')
    def save_build(self, build_id, **kwargs):
        build = request.env['pc.builds'].browse(build_id)
        if build.exists() and build.user_id.id == request.uid:
            request.env['saved.pc.builds'].create({
                'user_id': request.uid,
                'build_id': build_id,
            })
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Invalid build'}

    @http.route('/pc_builder/delete_saved_build', type='json', auth='user')
    def delete_saved_build(self, saved_build_id, **kwargs):
        saved_build = request.env['saved.pc.builds'].browse(saved_build_id)
        if saved_build.exists() and saved_build.user_id.id == request.uid:
            saved_build.unlink()
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Invalid saved build'}
```