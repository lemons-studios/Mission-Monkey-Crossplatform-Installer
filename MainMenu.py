from consolemenu import *
from consolemenu.items import *


def StartupText():
    startupMenu = ConsoleMenu("Main Menu", "Select what to do")
    menu_item = MenuItem("Menu Item")
    command_item = CommandItem("Run a console command", "touch hello.txt")
    function_item = FunctionItem("Call a Python function", input, ["Enter an input"])
    command_item = CommandItem("Run a console command", "touch hello.txt")
    selection_menu = SelectionMenu(["item1", "item2", "item3"])
    submenu_item = SubmenuItem("Submenu item", selection_menu, startupMenu)

    startupMenu.append_item(menu_item)
    startupMenu.append_item(function_item)
    startupMenu.append_item(command_item)
    startupMenu.append_item(submenu_item)

    startupMenu.show()
def SettingsMenu():
    print("Settings Menu")

