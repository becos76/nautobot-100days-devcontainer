from nautobot.apps.jobs import MultiChoiceVar, MultiObjectVar, Job, ObjectVar, register_jobs, StringVar, IntegerVar
from nautobot.dcim.models.devices import Device
from nautobot.dcim.models.locations import Location
import subprocess
import json 

name = "Operations with Ansible"

class HelloAnsible(Job):
    devices = MultiObjectVar(
        model=Device,
    )

    class Meta:
        name = "Ansible Hello World"
        description = "A job to call Ansible playbook."

    def run(self, devices):
        inventory = {"all": {"hosts": {}}}
        # Gather inventory information
        for device in devices:
            ip_address = str(device.primary_ip).split('/')[0] 
            inventory["all"]["hosts"][device.name] = {
                "ansible_host": ip_address,
                "ansible_user": "admin",  
                "ansible_password": "admin",
                "ansible_connection": "network_cli", 
                "ansible_network_os": "eos",
                "ansible_become": True,
                "ansible_become_method": "enable"
            }

        # Write the inventory to a temporary file
        inventory_file = "/tmp/inventory.json"
        with open(inventory_file, "w") as f:
            json.dump(inventory, f)

        # Run the Ansible playbook 
        device = str(device.primary_ip).split('/')[0]
        result = subprocess.run(
            ["ansible-playbook", "-i", inventory_file, "/opt/nautobot/jobs/hello_world.yml"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            self.logger.fatal(f"Ansible playbook failed: {result.stderr}")
            return

        self.logger.info(f"Successfully run ansible playbook, {result}.")


register_jobs(
    HelloAnsible,
)