"""Tables for nautobot_software_cves."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn, TagColumn
from django.urls import reverse
from nautobot_software_cves import models
from django.utils.safestring import mark_safe
from nautobot.dcim.models import SoftwareVersion


# class NautobotSoftwareCvesExampleModelTable(BaseTable):
#     # pylint: disable=R0903
#     """Table for list view."""

#     pk = ToggleColumn()
#     name = tables.Column(linkify=True)
#     actions = ButtonsColumn(
#         models.NautobotSoftwareCvesExampleModel,
#         # Option for modifying the default action buttons on each row:
#         # buttons=("changelog", "edit", "delete"),
#         # Option for modifying the pk for the action buttons:
#         pk_field="pk",
#     )

#     class Meta(BaseTable.Meta):
#         """Meta attributes."""

#         model = models.NautobotSoftwareCvesExampleModel
#         fields = (
#             "pk",
#             "name",
#             "description",
#         )

#         # Option for modifying the columns that show up in the list view by default:
#         # default_columns = (
#         #     "pk",
#         #     "name",
#         #     "description",
#         # )


class CveStatusTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = SoftwareVersion
        default_columns = ["platform", "version", "cves_count"]

    platform = tables.Column(linkify=True)
    version = tables.Column(linkify=True)
    cves_count = tables.Column(
        verbose_name="CVEs Count",
        empty_values=(),
        orderable=False
    )

    def render_cves_count(self, value, record):
        cves = record.custom_field_data.get('cves', {})
        if cves:
            url = reverse(
                "plugins:nautobot_software_cves:software_cves",
                kwargs={"pk": record.pk}
            )
            return mark_safe(f'<a href="{url}">{len(cves)}</a>')
        return 0

class CVETable(BaseTable):
    """Table for listing CVEs in the UI."""

    model = models.CVE
    pk = ToggleColumn()
    name = tables.Column(linkify=True)  # Allows clicking on the CVE name
    link = tables.TemplateColumn(
        template_code="""{% if record.link %}
            <a href="{{ record.link }}" target="_blank" data-toggle="tooltip" data-placement="left" title="{{ record.link }}">
                <span class="mdi mdi-open-in-new"></span>
            </a>
        {% else %}
            —
        {% endif %}""",
        verbose_name="Link",
    )
    actions = ButtonsColumn(models.CVE, buttons=("changelog", "edit", "delete"))
    tags = TagColumn(url_name="plugins:nautobot_software_cves:cve_list")

    class Meta(BaseTable.Meta):
        model = models.CVE
        fields = ("pk", "name", "link", "severity", "cvss", "affected_softwares", "actions")
        default_columns = ("pk", "name", "link", "severity", "cvss", "actions")