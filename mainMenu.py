import os
import random

import installAndUpdateGame

from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printMenu
from installAndUpdateGame import InstallationInformation
from miscMethods import clearScreen, MenuStyes
from art import  *

installInfo = InstallationInformation()
menuStyles = MenuStyes()


def menu():
    tprint("Mission: Monkey Installer", random.choice(menuStyles.AcceptedASCIIFonts))
    print("______________________________________________________________________________________")
    print("Select what you would like to do:")
    printMenu("1. Launch Mission: Monkey")
    printMenu("2. Install Mission: Monkey")
    printMenu("3. Check for updates")
    printMenu("4. Settings") # Contains Uninstall game method and repair game method for now
    printMenu("5. Quit")

    while True:
        try:
            choice = int(prompt("Select an option (1-5): "))
            if 0 <= choice <= 5:  # PyCharm decided to simplify my if statement like this
                break
            else:
                printMenu("Choose an option between 1 and 5!")
        except ValueError:
            printMenu("")

    match choice:  # I love swi- I mean match cases!!
        case 1:
            # Launches game if it exists

            pass
        case 2:
            # Calls the installation method
            clearScreen()
            print(f"Installing Mission Monkey {installInfo.latestBuildNum}.....")
            installAndUpdateGame.installGame()
            menu()
        case 3:
            # Checks for any updates by comparing the latest GitHub tag to the build number for the installation
            clearScreen()
            installAndUpdateGame.updateGame()
            menu()
            pass
        case 4:
            # Opens a new menu for settings
            clearScreen()
            SettingsMenu()
            pass
        case 5:
            # Quits the installer
            clearScreen()
            tprint("Goodbye", random.choice(menuStyles.AcceptedASCIIFonts))
            exit(0)


def SettingsMenu():
    tprint("Settings", random.choice(menuStyles.AcceptedASCIIFonts))
    print("______________________________________________________________________________________")
    printMenu("1. Repair/Reinstall Mission: Monkey")
    printMenu("2. Uninstall Mission: Monkey")
    printMenu("3. Back to Main Menu")

    while True:
        try:
            choice = int(prompt("Select an option (1-3): "))
            if 0 <= choice <= 3:
                break
            else:
                printMenu("Choose an option between 1 and 3!")
        except ValueError:
            printMenu("")
    match choice:
        case 1:
            installAndUpdateGame.repairInstallation()
            pass
        case 2:
            os.remove(installInfo.gameDirectory)
            print("game removed!")
            print("would you like to:")
            printMenu("1. Go back to Main Menu")
            printMenu("2. Quit")
            while True:
                try:
                    secondOptionChoice = int(prompt("1-2"))
                    if 0 <= choice <= 2:
                        break
                    else:
                        printMenu("Choose a value between 1 and 2")
                except ValueError:
                    printMenu("")
                match secondOptionChoice:
                    case 1:
                        clearScreen()
                        menu()
                    case 2:
                        clearScreen()
                        tprint("Goodbye!", random.choice(menuStyles.AcceptedASCIIFonts))

        case 3:
            clearScreen()
            menu()
            pass