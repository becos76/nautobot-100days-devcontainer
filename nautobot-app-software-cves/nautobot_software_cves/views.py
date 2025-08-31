from nautobot.apps import views
from nautobot.dcim.models import SoftwareVersion
from nautobot_software_cves.tables import CveStatusTable
from nautobot.dcim.filters import SoftwareVersionFilterSet
from nautobot_software_cves.tables import CveStatusTable
from nautobot_software_cves import filters, forms, models, tables
from nautobot_software_cves import serializers as software_cves_serializers

class SoftwareCvesStatusViewSet(views.ObjectListViewMixin):
    queryset = SoftwareVersion.objects.all()
    filterset_class = SoftwareVersionFilterSet
    table_class = CveStatusTable
    
class SoftwareCvesView(views.ObjectView):
    queryset = SoftwareVersion.objects.all()
    template_name = "nautobot_software_cves/software_cves.html"

    def get_extra_context(self, request, instance):
        return {"cves": instance.custom_field_data.get("cves", {})}

class CVEUIViewSet(views.NautobotUIViewSet):
    filterset_class = filters.CVEFilterSet
    form_class = forms.CVEForm
    lookup_field = "pk"
    queryset = models.CVE.objects.all()
    serializer_class = software_cves_serializers.CVESerializer
    table_class = tables.CVETable