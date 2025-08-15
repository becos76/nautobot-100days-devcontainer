"""App declaration for my_app."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class MyAppConfig(NautobotAppConfig):
    """App configuration for the my_app app."""

    name = "my_app"
    verbose_name = "My App"
    version = __version__
    author = "Manolis Kaliotis"
    description = "My App."
    base_url = "my-app"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:my_app:docs"


config = MyAppConfig  # pylint:disable=invalid-name
