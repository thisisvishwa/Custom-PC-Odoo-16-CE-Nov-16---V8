```python
from odoo import http

class PCBuildPreviewController(http.Controller):
    @http.route('/pc_build_preview/', auth='user')
    def index(self, **kw):
        pc_builds = http.request.env['custom_pc_builder.pc_builds']
        return http.request.render('custom_pc_builder.pc_build_preview_view', {
            'pc_builds': pc_builds.search([])
        })

    @http.route('/pc_build_preview/<model("custom_pc_builder.pc_builds"):pc_build>/', auth='user')
    def object(self, pc_build, **kw):
        return http.request.render('custom_pc_builder.pc_build_preview_view', {
            'pc_build': pc_build
        })

    @http.route('/pc_build_preview/update/', auth='user', method=['POST'], csrf=False)
    def update(self, **kw):
        pc_build = http.request.env['custom_pc_builder.pc_builds'].browse(int(kw.get('id')))
        pc_build.write({
            'component_ids': [(6, 0, [int(i) for i in kw.get('component_ids').split(',')])]
        })
        return http.request.redirect('/pc_build_preview/%s' % pc_build.id)
```