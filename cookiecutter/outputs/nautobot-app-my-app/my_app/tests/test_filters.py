"""Test MyAppExampleModel Filter."""

from nautobot.apps.testing import FilterTestCases

from my_app import filters, models
from my_app.tests import fixtures


class MyAppExampleModelFilterTestCase(FilterTestCases.FilterTestCase):
    """MyAppExampleModel Filter Test Case."""

    queryset = models.MyAppExampleModel.objects.all()
    filterset = filters.MyAppExampleModelFilterSet
    generic_filter_tests = (
        ("id",),
        ("created",),
        ("last_updated",),
        ("name",),
    )

    @classmethod
    def setUpTestData(cls):
        """Setup test data for MyAppExampleModel Model."""
        fixtures.create_myappexamplemodel()

    def test_q_search_name(self):
        """Test using Q search with name of MyAppExampleModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for MyAppExampleModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
