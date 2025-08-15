"""Django urlpatterns declaration for my_app app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter


from my_app import views


app_name = "my_app"
router = NautobotUIViewSetRouter()

# The standard is for the route to be the hyphenated version of the model class name plural.
# for example, ExampleModel would be example-models.
router.register("my-app-example-models", views.MyAppExampleModelUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("my_app/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
