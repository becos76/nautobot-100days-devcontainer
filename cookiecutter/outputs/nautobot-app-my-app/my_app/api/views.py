"""API views for my_app."""

from nautobot.apps.api import NautobotModelViewSet

from my_app import filters, models
from my_app.api import serializers


class MyAppExampleModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """MyAppExampleModel viewset."""

    queryset = models.MyAppExampleModel.objects.all()
    serializer_class = serializers.MyAppExampleModelSerializer
    filterset_class = filters.MyAppExampleModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
