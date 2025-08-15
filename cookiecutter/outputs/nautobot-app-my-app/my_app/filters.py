"""Filtering for my_app."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from my_app import models


class MyAppExampleModelFilterSet(NameSearchFilterSet, NautobotFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for MyAppExampleModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.MyAppExampleModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
