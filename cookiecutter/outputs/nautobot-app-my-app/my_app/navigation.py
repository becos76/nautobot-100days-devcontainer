"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:my_app:myappexamplemodel_list",
        name="My App",
        permissions=["my_app.view_myappexamplemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:my_app:myappexamplemodel_add",
                permissions=["my_app.add_myappexamplemodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="My App", items=tuple(items)),),
    ),
)
