from django.contrib import admin

from nautobot.apps.admin import NautobotModelAdmin

from example_app.models import ExampleModel, UsefulLink


@admin.register(ExampleModel)
class ExampleModelAdmin(NautobotModelAdmin):
    list_display = ("name", "number")


@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ("url", "description")
    search_fields = ("url", "description")
