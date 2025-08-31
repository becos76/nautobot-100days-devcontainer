from nautobot.apps.ui import NavMenuGroup, NavMenuItem, NavMenuTab

menu_items = (
    NavMenuTab(
        name="Devices",
        groups=(
            NavMenuGroup(
                name="Software",
                items=(
                    NavMenuItem(
                        # link="plugins:nautobot_software_cves:softwareversions", # Explained Below
                        link="plugins:nautobot_software_cves:softwareversion_list",
                        name="CVE Status",
                        permissions=["dcim.view_softwareversion"],
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="CVE Tracking",
        groups=(
            NavMenuGroup(
                name="CVEs",
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_software_cves:cve_list",
                        name="CVEs",
                        permissions=["nautobot_software_cves.cve"],
                    ),
                ),
            ),
        ),
    ),
)