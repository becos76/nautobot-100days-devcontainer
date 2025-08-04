from nautobot.apps.jobs import Job, register_jobs, FileVar   
from nautobot.dcim.models import Device, Location, DeviceType
from nautobot.extras.models import Role, Status


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

class FileUpload_2(Job):
    class Meta:
        name = "CSV File Upload and Process"
        description = "Please select a CSV file for upload"

    file = FileVar(
        description="CSV file to upload",
    )

    def run(self, file):
        file_contents = str(file.read().decode('utf-8'))
        self.logger.info(f"File contents: {file_contents}")
        lines = file_contents.splitlines()

        self.logger.info(f"Parsing of the lines")

        for line in lines[1:]:  # Skip header
            device_name, role_name, model_name, location_name = line.split(",")
            self.logger.info(f"Name: {device_name}")
            self.logger.info(f"Role: {role_name}")
            self.logger.info(f"Device Type: {model_name}")
            self.logger.info(f"Location: {location_name}")

            role = Role.objects.get(name=role_name)
            location = Location.objects.get(name=location_name)
            device_type = DeviceType.objects.get(model=model_name)
            status = Status.objects.get(name="Active")

            device = Device(
                name=device_name,
                role=role,
                location=location,
                device_type=device_type,
                status=status,
            )
            device.validated_save()
            
        return "Execution completed"

register_jobs(
    FileUpload,
    FileUpload_2
)