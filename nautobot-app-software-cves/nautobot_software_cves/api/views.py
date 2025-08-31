from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from nautobot.dcim.models import SoftwareVersion


class SoftwareVersionCVEsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        software_version = get_object_or_404(
            SoftwareVersion.objects.restrict(self.request.user, "view"), pk=pk
        )
        custom_field_data = software_version.custom_field_data
        return Response({"cves": custom_field_data.get("cves", {})})