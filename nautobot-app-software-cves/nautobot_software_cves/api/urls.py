from django.urls import path
from nautobot_software_cves.api.views import SoftwareVersionCVEsView

urlpatterns = [
    path(
        "softwareversions/<uuid:pk>/cves/",
        SoftwareVersionCVEsView.as_view(),
        name="software_cves",
    ),
]

# urlpatterns = router.urls