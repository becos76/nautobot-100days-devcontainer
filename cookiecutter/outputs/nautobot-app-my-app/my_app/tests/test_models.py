"""Test MyAppExampleModel."""

from nautobot.apps.testing import ModelTestCases

from my_app import models
from my_app.tests import fixtures


class TestMyAppExampleModel(ModelTestCases.BaseModelTestCase):
    """Test MyAppExampleModel."""

    model = models.MyAppExampleModel

    @classmethod
    def setUpTestData(cls):
        """Create test data for MyAppExampleModel Model."""
        super().setUpTestData()
        # Create 3 objects for the model test cases.
        fixtures.create_myappexamplemodel()

    def test_create_myappexamplemodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        myappexamplemodel = models.MyAppExampleModel.objects.create(name="Development")
        self.assertEqual(myappexamplemodel.name, "Development")
        self.assertEqual(myappexamplemodel.description, "")
        self.assertEqual(str(myappexamplemodel), "Development")

    def test_create_myappexamplemodel_all_fields_success(self):
        """Create MyAppExampleModel with all fields."""
        myappexamplemodel = models.MyAppExampleModel.objects.create(name="Development", description="Development Test")
        self.assertEqual(myappexamplemodel.name, "Development")
        self.assertEqual(myappexamplemodel.description, "Development Test")
