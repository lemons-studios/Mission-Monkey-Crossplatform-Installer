from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text as printMenu
from latestBuild import GetLatestBuildNumber

def menu():
    # Some help from mister GPT for making the menu code but the rest is mine
    printMenu(f"Welcome to the Mission: Monkey cross-platform installer! (Version 0.1)")
    printMenu("Select what you would like to do:")
    printMenu("1. Install Mission: Monkey")
    printMenu("2. Check for updates")
    printMenu("3. Settings")
    printMenu("4. Quit")

    while True:
        try:
            choice = int(prompt("Select an options (1-4:) "))
            if 0 <= choice <= 4:  # PyCharm decided to simplify my if statement like this
                break
            else:
                printMenu("Choose an option between 1 and 4!")
        except ValueError:
            printMenu("The input you entered is not valid!")

    match choice:  # I love swi- I mean match cases!!
        case 1:
            # Calls the installation method

            pass
        case 2:
            # Checks for any updates by comparing the latest GitHub tag to the build number for the installation

            pass
        case 3:
            # Opens a new menu for settings

            pass
        case 4:
            # Quits the installer
            printMenu("Goodbye.")
            exit(0)
