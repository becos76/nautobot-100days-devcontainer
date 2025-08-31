"""App declaration for nautobot_software_cves."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class NautobotSoftwareCvesConfig(NautobotAppConfig):
    """App configuration for the nautobot_software_cves app."""

    name = "nautobot_software_cves"
    verbose_name = "Nautobot Software Cves"
    version = __version__
    author = "Manolis Kaliotis"
    description = "Nautobot Software Cves."
    base_url = "software-cves"
    required_settings = []
    min_version = "2.3.2"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:nautobot_software_cves:docs"


config = NautobotSoftwareCvesConfig  # pylint:disable=invalid-name
