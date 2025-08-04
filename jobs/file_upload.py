from nautobot.apps.jobs import Job, register_jobs, FileVar   

class FileUpload(Job):
    class Meta:
        name = "CSV File Upload"
        description = "Please select a CSV file for upload"
    
    file = FileVar(
        description="CSV file to upload",
    )

    def run(self, file):
        contents = str(file.read())
        self.logger.info(f"File contents: {contents}")
        self.logger.info("Job didn't crash!")

        return "Great Job!!"

register_jobs(
    FileUpload,
)