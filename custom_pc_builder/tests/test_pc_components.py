```python
from odoo.tests import common

class TestPCComponents(common.TransactionCase):

    def setUp(self):
        super(TestPCComponents, self).setUp()
        self.PCComponents = self.env['pc.components']

    def test_create_pc_component(self):
        """
        Test the creation of a PC component
        """
        pc_component = self.PCComponents.create({
            'name': 'Test Component',
            'component_type': 'CPU',
            'specifications': 'Test Specifications',
        })

        self.assertEqual(pc_component.name, 'Test Component')
        self.assertEqual(pc_component.component_type, 'CPU')
        self.assertEqual(pc_component.specifications, 'Test Specifications')

    def test_update_pc_component(self):
        """
        Test the update of a PC component
        """
        pc_component = self.PCComponents.create({
            'name': 'Test Component',
            'component_type': 'CPU',
            'specifications': 'Test Specifications',
        })

        pc_component.write({
            'name': 'Updated Component',
            'component_type': 'GPU',
            'specifications': 'Updated Specifications',
        })

        self.assertEqual(pc_component.name, 'Updated Component')
        self.assertEqual(pc_component.component_type, 'GPU')
        self.assertEqual(pc_component.specifications, 'Updated Specifications')

    def test_delete_pc_component(self):
        """
        Test the deletion of a PC component
        """
        pc_component = self.PCComponents.create({
            'name': 'Test Component',
            'component_type': 'CPU',
            'specifications': 'Test Specifications',
        })

        pc_component.unlink()

        self.assertEqual(len(self.PCComponents.search([('name', '=', 'Test Component')])), 0)
```