"""Forms for my_app."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from my_app import models


class MyAppExampleModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """MyAppExampleModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.MyAppExampleModel
        fields = "__all__"


class MyAppExampleModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """MyAppExampleModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.MyAppExampleModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class MyAppExampleModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.MyAppExampleModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name.",
    )
    name = forms.CharField(required=False, label="Name")
