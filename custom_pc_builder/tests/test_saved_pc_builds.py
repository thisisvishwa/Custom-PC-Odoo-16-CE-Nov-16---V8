```python
from odoo.tests import common

class TestSavedPcBuilds(common.TransactionCase):

    def setUp(self):
        super(TestSavedPcBuilds, self).setUp()
        self.SavedPcBuilds = self.env['saved.pc.builds']

    def test_check_saved_pc_builds(self):
        # Create a new saved PC build
        saved_pc_build = self.SavedPcBuilds.create({
            'name': 'Test Build',
            'user_id': 1,
            'pc_build_id': 1,
        })

        # Check if the saved PC build is created
        self.assertEqual(saved_pc_build.name, 'Test Build')

        # Check if the user ID is correct
        self.assertEqual(saved_pc_build.user_id.id, 1)

        # Check if the PC build ID is correct
        self.assertEqual(saved_pc_build.pc_build_id.id, 1)

    def test_check_saved_pc_builds_constraints(self):
        # Try to create a saved PC build with invalid user ID
        with self.assertRaises(ValueError):
            self.SavedPcBuilds.create({
                'name': 'Test Build',
                'user_id': 0,
                'pc_build_id': 1,
            })

        # Try to create a saved PC build with invalid PC build ID
        with self.assertRaises(ValueError):
            self.SavedPcBuilds.create({
                'name': 'Test Build',
                'user_id': 1,
                'pc_build_id': 0,
            })
```