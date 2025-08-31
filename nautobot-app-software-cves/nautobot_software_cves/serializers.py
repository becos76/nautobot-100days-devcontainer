from nautobot.apps.api import NautobotModelSerializer
from nautobot_software_cves.models import CVE

class CVESerializer(NautobotModelSerializer):
    class Meta:
        model = CVE
        fields = ["__all__"]