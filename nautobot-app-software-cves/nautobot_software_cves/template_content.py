"""Module to change object details view."""

from django.urls import reverse
from nautobot.apps.ui import TemplateExtension

class SoftwareVersionTemplateExtension(TemplateExtension):

    model = "dcim.softwareversion"

    def right_page(self):
        """Add content on the right side of the view."""
        # Get the object that was provided as template context;
        # in this case, the SoftwareVersion object itself.
        software_version = self.context["object"]
        
        # Get the CVEs from the JSON Custom Field:
        cves = software_version.custom_field_data.get("cves", {})
        
        # Construct the HTML to contain this data
        output = """
            <div class="panel panel-default">
            <div class="panel-heading"><strong>CVEs</strong></div>
            <div class="panel-body">
        """
        
        # Add list entries based on the available data:
        if cves:
            output += "<ul>"
            for cve_name, cve_data in cves.items():
                output += f"<li><a href='{cve_data['link']}' target='_blank'> {cve_name}</a></li>"
            output += "</ul>"
        else:
            output += "There are no CVEs for this Software Version."
        
        output += "</div></div>"
        return output

    def detail_tabs(self): #new
        """Add a CVE details tab to the SoftwareVersion view."""
        return [
            {
                "title": "CVEs",
                "url": reverse(
                    "plugins:nautobot_software_cves:software_cves",
                    kwargs={"pk": self.context["object"].pk}
                ),
            },
        ]




template_extensions = [SoftwareVersionTemplateExtension]
