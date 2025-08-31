import django_filters
from nautobot.apps.filters import NautobotFilterSet, SearchFilter, TagFilter
from nautobot_software_cves.models import CVE

class CVEFilterSet(NautobotFilterSet):
    class Meta:
        model = CVE
        fields = ["name", "cvss"]

    q = SearchFilter(filter_predicates={"name": "icontains"})
    cvss__gte = django_filters.NumberFilter(field_name="cvss", lookup_expr="gte")
    cvss__lte = django_filters.NumberFilter(field_name="cvss", lookup_expr="lte")
    tags = TagFilter()