""" 
Module for managing CVEs in Nautobot using NIST NVD API.

This module defines a job for loading CVEs into Nautobot\'s database.
"""

import requests

from nautobot.apps.jobs import BooleanVar, Job, ObjectVar, MultiObjectVar, register_jobs
from nautobot.extras.models import ExternalIntegration
from nautobot.dcim.models.devices import SoftwareVersion, SoftwareVersionQuerySet
from nautobot_software_cves.models import CVE

name = "CVE Tracking"


# class LoadCVEsJob(Job):
#     nist_external_integration = ObjectVar(
#         model=ExternalIntegration,
#         label="NIST NVD API",
#         description="External Integration for CVE portal of NIST NVD database",
#         required=True,
#     )
#     softwares = MultiObjectVar(
#         model=SoftwareVersion,
#         label="Softwares",
#         description="Load CVEs for the selected softwares.",
#         required=False
#     )
#     debug = BooleanVar(description="Enable for more verbose debug logging")

#     class Meta:
#         """Meta object for Device State Diff - Compare Data Job."""

#         name = "Load Vulnerabilities"
#         description = "Load Vulnerabilities"
#         has_sensitive_variables = False
#         hidden = False

#     def run(
#         self,
#         nist_external_integration: ExternalIntegration = None,
#         softwares: SoftwareVersionQuerySet = None,
#         debug: bool = False,
#     ):

#         # Set logging level
#         self.logger.setLevel("DEBUG" if debug else "INFO")

#         # Define the SoftwareVersion queryset if user hasn't selected any software
#         if not softwares:
#             softwares = SoftwareVersion.objects.all()

#         # Loop over the selected softwares to load the CVEs
#         for software in softwares:
#             self.logger.info("Loading CVEs from NIST NVD Database", extra={"object": software})

#             # Retrieve Software Vulnerabilities from NIST NVD API
#             software_version = software.version
#             cpe_name = f"cpe:2.3:o:cisco:ios_xe:{software_version}:*:*:*:*:*:*:*"
#             url = nist_external_integration.remote_url
#             params = {"cpeName": cpe_name}
#             headers = nist_external_integration.headers
#             timeout = nist_external_integration.timeout
#             http_method = nist_external_integration.http_method
#             try:
#                 response = requests.request(
#                     method=http_method,
#                     url=url,
#                     headers=headers,
#                     params=params,
#                     timeout=timeout
#                 )
#                 # Raise an exception for 4xx/5xx responses
#                 response.raise_for_status()
#                 # Parse JSON response and get the vulnerabilities
#                 data = response.json()
#                 self.logger.debug(f"NVD Response: {data}")
#                 vulnerabilities = data.get('vulnerabilities', [])
#             except Exception as e:
#                 self.logger.error(f"Unexpected error: {e}")
#                 vulnerabilities = []

#             # initialize the custom field data if it is None
#             if not software.custom_field_data['cves']:
#                 software.custom_field_data['cves'] = {}

#             # Loop over the vulnerabilities and load them into Nautobot
#             for cve in vulnerabilities:
#                 cve_name = cve['cve']['id']
#                 self.logger.info(f"Loading CVE {cve_name}", extra={"object": software})
#                 cvss_versions = ['cvssMetricV32', 'cvssMetricV31', 'cvssMetricV30']
#                 cvss_version = next(version for version in cvss_versions if version in cve['cve']['metrics'])
#                 software.custom_field_data['cves'][cve_name] = {
#                      "cvss_base_score": cve['cve']['metrics'][cvss_version][0]['cvssData']['baseScore'],
#                      "link": cve['cve']['references'][0]['url'],
#                      "severity": cve['cve']['metrics'][cvss_version][0]['cvssData']['baseSeverity'],
#                  }
#                 software.validated_save()

class LoadCVEsJob(Job):
    nist_external_integration = ObjectVar(
        model=ExternalIntegration,
        label="NIST NVD API",
        description="External Integration for CVE portal of NIST NVD database",
        required=True,
    )
    softwares = MultiObjectVar(
        model=SoftwareVersion,
        label="Softwares",
        description="Load CVEs for the selected softwares.",
        required=False
    )
    debug = BooleanVar(description="Enable for more verbose debug logging")

    class Meta:
        name = "Load Vulnerabilities"
        description = "Load Vulnerabilities"
        has_sensitive_variables = False
        hidden = False

    def run(
        self,
        nist_external_integration: ExternalIntegration = None,
        softwares: SoftwareVersionQuerySet = None,
        debug: bool = False,
    ):
        self.logger.setLevel("DEBUG" if debug else "INFO")

        if not softwares:
            softwares = SoftwareVersion.objects.all()

        for software in softwares:
            self.logger.info("Loading CVEs from NIST NVD Database", extra={"object": software})

            software_version = software.version
            cpe_name = f"cpe:2.3:o:cisco:ios_xe:{software_version}:*:*:*:*:*:*:*"
            url = nist_external_integration.remote_url
            params = {"cpeName": cpe_name}
            headers = nist_external_integration.headers
            timeout = nist_external_integration.timeout
            http_method = nist_external_integration.http_method

            try:
                response = requests.request(
                    method=http_method,
                    url=url,
                    headers=headers,
                    params=params,
                    timeout=timeout
                )
                response.raise_for_status()
                data = response.json()
                self.logger.debug(f"NVD Response: {data}")
                vulnerabilities = data.get('vulnerabilities', [])
            except Exception as e:
                self.logger.error(f"Unexpected error: {e}")
                vulnerabilities = []

            for cve in vulnerabilities:
                cve_name = cve['cve']['id']
                self.logger.info(f"Loading CVE {cve_name}", extra={"object": software})

                cvss_versions = ['cvssMetricV32', 'cvssMetricV31', 'cvssMetricV30']
                cvss_version = next(version for version in cvss_versions if version in cve['cve']['metrics'])
                # software.custom_field_data['cves'][cve_name] = {
                #     "cvss_base_score": cve['cve']['metrics'][cvss_version][0]['cvssData']['baseScore'],
                #     "link": cve['cve']['references'][0]['url'],
                #     "severity": cve['cve']['metrics'][cvss_version][0]['cvssData']['baseSeverity'],
                # }
                # software.validated_save()
                cve_obj, created = CVE.objects.get_or_create(
                    name = cve_name,
                    defaults = {
                        'cvss' : cve['cve']['metrics'][cvss_version][0]['cvssData']['baseScore'],
                        'severity' : cve['cve']['metrics'][cvss_version][0]['cvssData']['baseSeverity'].capitalize(),
                        'link' : cve['cve']['references'][0]['url'],
                    }
                )
                cve_obj.affected_softwares.add(software)



jobs = [LoadCVEsJob]
register_jobs(*jobs)