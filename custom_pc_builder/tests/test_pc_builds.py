```python
from odoo.tests import common

class TestPCBuilds(common.TransactionCase):

    def setUp(self):
        super(TestPCBuilds, self).setUp()
        self.PCBuilds = self.env['pc_builds']

    def test_create_pc_build(self):
        """
        Test the creation of a PC build
        """
        pc_build = self.PCBuilds.create({
            'user_id': 1,
            'component_ids': [(6, 0, [1, 2, 3])],
            'configuration': 'Test configuration',
        })
        self.assertEqual(pc_build.user_id.id, 1)
        self.assertEqual(len(pc_build.component_ids), 3)
        self.assertEqual(pc_build.configuration, 'Test configuration')

    def test_update_pc_build(self):
        """
        Test the update of a PC build
        """
        pc_build = self.PCBuilds.create({
            'user_id': 1,
            'component_ids': [(6, 0, [1, 2, 3])],
            'configuration': 'Test configuration',
        })
        pc_build.write({
            'user_id': 2,
            'component_ids': [(6, 0, [4, 5, 6])],
            'configuration': 'Updated configuration',
        })
        self.assertEqual(pc_build.user_id.id, 2)
        self.assertEqual(len(pc_build.component_ids), 3)
        self.assertEqual(pc_build.configuration, 'Updated configuration')

    def test_delete_pc_build(self):
        """
        Test the deletion of a PC build
        """
        pc_build = self.PCBuilds.create({
            'user_id': 1,
            'component_ids': [(6, 0, [1, 2, 3])],
            'configuration': 'Test configuration',
        })
        pc_build.unlink()
        self.assertEqual(len(self.PCBuilds.search([])), 0)
```