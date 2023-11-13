import os
import platform
import random
import installAndUpdateGame
import subprocess

from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printMenu
from installAndUpdateGame import InstallationInformation
from miscMethods import clearScreen, MenuStyes, deleteDirectory
from art import  *


installInfo = InstallationInformation()
menuStyles = MenuStyes()


def menu():
    tprint("Mission: Monkey Installer", random.choice(menuStyles.AcceptedASCIIFonts)) # Picks a random font from the menuStyles class (The random font being a list of ASCII fonts that I like)
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

            if platform.system() == 'Windows':
                executable = (os.path.join(installInfo.gameDirectory, 'Mission Monkey.exe'))
            elif platform.system() == 'Darwin':  # MacOS
                executable =(os.path.join(installInfo.gameDirectory, 'Mission Monkey.app'))
            elif platform.system() == 'Linux':
                executable = (os.path.join(installInfo.gameDirectory, 'Mission Monkey.x86_64'))
            
            if(os.path.exists(executable)):
                subprocess.Popen(executable)
            else:
                print("Error: Executable not found! please repair your installation!")
        case 2:
            # Calls the installation method
            clearScreen()
            print(f"Installing Mission Monkey {installInfo.latestBuildNum}.....")
            installAndUpdateGame.installGame(installInfo.downloadURL)
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
            menu()
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
            # Calls the repair install method
            installAndUpdateGame.repairInstallation()
            print("Installation Repaired!")
            pass
        case 2:
            # Deletes the Mission: Monkey installation directory (~/Mission-Monkey)
            clearScreen()
            deleteDirectory(installInfo.gameDirectory)
            print("Game Uninstalled!")

        case 3:
            # Go back to main menu
            clearScreen()