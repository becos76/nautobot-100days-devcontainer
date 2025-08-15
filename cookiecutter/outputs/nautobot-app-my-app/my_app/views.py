"""Views for my_app."""

from nautobot.apps.views import NautobotUIViewSet

from my_app import filters, forms, models, tables
from my_app.api import serializers


class MyAppExampleModelUIViewSet(NautobotUIViewSet):
    """ViewSet for MyAppExampleModel views."""

    bulk_update_form_class = forms.MyAppExampleModelBulkEditForm
    filterset_class = filters.MyAppExampleModelFilterSet
    filterset_form_class = forms.MyAppExampleModelFilterForm
    form_class = forms.MyAppExampleModelForm
    lookup_field = "pk"
    queryset = models.MyAppExampleModel.objects.all()
    serializer_class = serializers.MyAppExampleModelSerializer
    table_class = tables.MyAppExampleModelTable
