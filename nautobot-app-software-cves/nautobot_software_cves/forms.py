from django import forms
from nautobot.apps.forms import NautobotModelForm, DynamicModelMultipleChoiceField
from nautobot.dcim.models import SoftwareVersion
from nautobot_software_cves.models import CVE, CVESeverityChoices

class CVEForm(NautobotModelForm):
    """Form for creating and editing CVEs."""

    severity = forms.ChoiceField(choices=CVESeverityChoices.CHOICES, label="Severity", required=False)
    affected_softwares = DynamicModelMultipleChoiceField(queryset=SoftwareVersion.objects.all(), required=False)

    class Meta:
        model = CVE
        fields = "__all__"