from django.db import models

try:
    from nautobot.apps.constants import CHARFIELD_MAX_LENGTH
except ImportError:
    CHARFIELD_MAX_LENGTH = 255

from nautobot.apps.models import PrimaryModel
from nautobot.apps.choices import ChoiceSet

class CVESeverityChoices(ChoiceSet):
    """Choices for CVE severity levels."""

    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    NONE = "None"

    CHOICES = (
        (CRITICAL, CRITICAL),
        (HIGH, HIGH),
        (MEDIUM, MEDIUM),
        (LOW, LOW),
        (NONE, NONE),
    )

class CVE(PrimaryModel):
    """Model representing a CVE."""

    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH, unique=True)
    link = models.URLField()
    severity = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        choices=CVESeverityChoices,
        default=CVESeverityChoices.NONE
    )
    cvss = models.FloatField(null=True, blank=True, verbose_name="CVSS Base Score")
    affected_softwares = models.ManyToManyField(
        to="dcim.SoftwareVersion",
        related_name="corresponding_cves",
        blank=True
    )

    class Meta:
        verbose_name = "CVE"
        ordering = ("severity", "name")

    def __str__(self):
        return self.name