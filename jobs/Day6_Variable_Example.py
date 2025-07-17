from nautobot.apps.jobs import MultiChoiceVar, Job, ObjectVar, register_jobs, TextVar, IntegerVar
from nautobot.dcim.models.locations import Location 


name = "Day 6 Variables"

class HelloVariables(Job):

    message = TextVar()
    days = IntegerVar(
        default="10",
    )
    CHOICES = (
        ("h", "Happy"),
        ("s", "Sad"),
        ("e", "Excited"),
    )
    feelings = MultiChoiceVar(
        choices=CHOICES,
        default=["h"],
        label="Feelings",
        description="Select your feelings.",
    )
    location = ObjectVar(
        model=Location,
        required=False,
        label="Location",
        description="Select a location if you want.",
    )
    class Meta:
        name = "Hello Variables"
        description = "Jobs Variable Examples"

    def run(self, message, days, feelings, location):
        self.logger.debug(f"Please give the message: {message} in {days} days.")
        self.logger.debug(f"I am feeling {feelings}!")
        self.logger.info(f"Location is: {location if location else 'No location selected'}.")
register_jobs(
    HelloVariables,
)
