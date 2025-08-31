"""Django urlpatterns declaration for nautobot_software_cves app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView

from nautobot.apps.urls import NautobotUIViewSetRouter


# Uncomment the following line if you have views to import
from nautobot_software_cves import views


app_name = "nautobot_software_cves"
router = NautobotUIViewSetRouter()
router.register("softwareversions", views.SoftwareCvesStatusViewSet)
router.register("cves", views.CVEUIViewSet) # New Routing for CVE model

# Here is an example of how to register a viewset, you will want to replace views.NautobotSoftwareCvesUIViewSet with your viewset
# router.register("nautobot_software_cves", views.NautobotSoftwareCvesUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("nautobot_software_cves/docs/index.html")), name="docs"),
    path(
        "softwareversions/<uuid:pk>/cves/",
        views.SoftwareCvesView.as_view(),
        name="software_cves",
    ),
]

urlpatterns += router.urls
