from nautobot.apps.jobs import Job, register_jobs
from nautobot.extras.models import JobLogEntry

name = "Log Jobs"

class DeleteInfoLogEntries(Job):
    class Meta:
        name = "Delete Information Level Log Entries"
        description = "A job to delete all information level log entries"
    
    def run(self):
        # Filter for information log entries
        info_log_entries = JobLogEntry.objects.filter(log_level="info")

        # Log the number of entires to be deleted
        info_entries_count = info_log_entries.count()
        self.logger.debug(f"Found {info_entries_count} information log entries to delete.")

        # Delete the filtered log entries
        deleted_count, _ = info_log_entries.delete()

        # Log the result of the deletion
        self.logger.debug(f"Deleted {deleted_count} information level log entries.")

register_jobs(
    DeleteInfoLogEntries,
)
