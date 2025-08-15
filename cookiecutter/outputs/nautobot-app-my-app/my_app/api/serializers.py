"""API serializers for my_app."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from my_app import models


class MyAppExampleModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """MyAppExampleModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.MyAppExampleModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
