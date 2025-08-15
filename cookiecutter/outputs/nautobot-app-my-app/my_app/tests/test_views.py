"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from my_app import models
from my_app.tests import fixtures


class MyAppExampleModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the MyAppExampleModel views."""

    model = models.MyAppExampleModel
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }

    update_data = {
        "name": "Test 2",
        "description": "Updated model",
    }

    @classmethod
    def setUpTestData(cls):
        fixtures.create_myappexamplemodel()
