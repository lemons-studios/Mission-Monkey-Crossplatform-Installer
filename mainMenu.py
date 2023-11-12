import random

import installAndUpdateGame

from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printMenu
from installAndUpdateGame import InstallationInformation
from latestBuild import clearScreen
from art import  *

installInfo = InstallationInformation()
# Art library has a argument that allows random ascii font generation, but I do not like some of the fonts, so this list containing any of the fonts will be used instead
AcceptedASCIIFonts = \
[
    "3-d", "64f1", "6x10", "6x9", "advenger", "amcaa01",
    "alphabet", "amcrazo2", "amcrazor", "amcslash", "amctubes",
    "amcun1", "aquaplan", "arrows", "asc", "avatar", "barbwire", "basic",
    "bell", "big", "bigfig", "bolger", "braced", "bulbhead", "char4", "charact3",
    "charact4", "chunky", "clr6x6", "coinstak", "cola", "colossal", "computer", "contrast",
    "crawford", "cricket", "cybermedium", "dietcola", "doom", "double", "drpepper", "druid",
    "eftifont", "eftirobot", "eftiwater", "epic", "fantasy", "filter", "fire_font-s", "flipped",
    "future_4", "future_6", "future_8", "graffiti", "greek", "henry3d", "jacky", "jazmine", "katakana",
    "letters", "lineblocks", "modular", "nancyj",  "nancyj-fancy", "ogre", "os2",  "pawp", "peaks",
    "puffy",  "rectangles", "red_phoenix", "rounded",  "script", "serifcap", "slant",  "small",
    "smallcaps", "smkeyboard",  "smpoison", "smslant", "soft",  "standard", "starwars", "stforek",
    "thin", "tinker-toy", "tubular",  "unarmed", "utopia", "xtimes"
]

def menu():
    tprint("Mission: Monkey Installer", random.choice(AcceptedASCIIFonts))
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
            printMenu("  ")

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

            pass
        case 5:
            # Quits the installer
            clearScreen()
            exit(0)
