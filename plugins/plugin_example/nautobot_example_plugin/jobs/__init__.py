from nautobot.core.celery import register_jobs
from .verify_hostnames import VerifyHostnameJob

jobs = [VerifyHostnameJob]
register_jobs(*jobs)
