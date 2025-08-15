"""Create fixtures for tests."""

from my_app.models import MyAppExampleModel


def create_myappexamplemodel():
    """Fixture to create necessary number of MyAppExampleModel for tests."""
    MyAppExampleModel.objects.create(name="Test One")
    MyAppExampleModel.objects.create(name="Test Two")
    MyAppExampleModel.objects.create(name="Test Three")
