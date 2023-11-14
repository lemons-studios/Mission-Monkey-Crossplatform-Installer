import platform
import os
import shutil
import requests

from tqdm import tqdm
from miscMethods import getLatestTag, clearScreen, deleteDirectory, MenuStyles

menuStyles = MenuStyles()


class InstallationInformation:
    latestBuildNum = getLatestTag("Mission-Monkey")
    clientPlatform = platform.system()
    gameDirectory = None
    gameData = None

    if platform.system() != "Windows":
        gameDirectory = os.path.join(os.path.expanduser("~"), "Mission-Monkey")
    else:
        gameDirectory = os.path.join(os.environ['USERPROFILE'], "Mission-Monkey")

    gameData = os.path.join(gameDirectory, 'game.zip')
    buildInfo = f'{gameDirectory}/buildInfo.txt'
    downloadURL = f"https://github.com/lemons-studios/Mission-Monkey/releases/download/{latestBuildNum}/{latestBuildNum}-{clientPlatform}.zip"


installInfo = InstallationInformation()


def installGame(Url):
    # The user might try to install the game after uninstalling without relaunching the installer application, so check if the installation directory exists before the installation begins
    if not os.path.exists(installInfo.gameDirectory) or not os.path.exists(installInfo.buildInfo):
        os.mkdir(installInfo.gameDirectory)
        with open(installInfo.buildInfo, 'w') as latestBuild:
            latestBuild.write(getLatestTag("Mission-Monkey"))
    # This download + progressbar code was borrowed from StackOverflow (https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests)
    # Download game and show progress with tqdm
    response = requests.get(Url, stream=True)
    totalSize = int(response.headers.get('content-length'), 0)
    blockSize = 1024  # 1 Kilobyte
    progressBar = tqdm(total=totalSize, unit="iB", unit_scale=True)
    with open(installInfo.gameData, 'wb') as archivedGame:
        for data in response.iter_content(blockSize):
            progressBar.update(len(data))
            archivedGame.write(data)
    progressBar.close()
    if totalSize != 0 and progressBar.n != totalSize:
        print("Something terrible happened. Try downloading again?")

    # Extract the downloaded zip file with shutil
    print("Extracting game")
    shutil.unpack_archive(installInfo.gameData, installInfo.gameDirectory)
    os.remove(installInfo.gameData)  # Delete the game zip archive after downloading

    # If on Linux, give the game executable the permissions to run itself
    if platform.system() == 'Linux':
        os.system(f"chmod 777 ~/Mission-Monkey/Mission-Monkey.x86_64")

    # TODO: make a prompt asking the user what to do after the install is done
    # TODO: Create a shortcut on the desktop of the user account running the application
    clearScreen()
    return


def updateGame():
    # TODO: make a prompt asking the user what to do after the update is done
    if os.path.exists(installInfo.gameDirectory) and os.path.exists(installInfo.buildInfo):
        installedBuild = open(f'{installInfo.gameDirectory}/buildInfo.txt').readline()
        if installedBuild != installInfo.latestBuildNum:
            print(f"There is a new version available ({installInfo.latestBuildNum})! ")
            deleteDirectory(installInfo.gameDirectory)

            os.mkdir(installInfo.gameDirectory)
            with open(installInfo.buildInfo, 'w') as latestBuild:
                latestBuild.write(installInfo.latestBuildNum)
            installGame(installInfo.downloadURL)
        else:
            print("You have the latest version of Mission: Monkey installed on your computer")
    else:
        print("Error: Game not installed. Please install the game first!")


def repairInstallation():
    # Delete any files in the installation directory (except for the build info file), and call the installGame method after to download the new version of the game
    # TODO: make a prompt asking the user what to do after the reinstall is done
    with open(installInfo.buildInfo) as buildInfo:
        installedVersion = buildInfo.readline()
    deleteDirectory(installInfo.gameDirectory)
    os.mkdir(installInfo.gameDirectory)
    with open(installInfo.buildInfo, 'w') as previousBuild:
        previousBuild.write(installedVersion)

    installGame(
        f"https://github.com/lemons-studios/Mission-Monkey/releases/download/{installedVersion}/{installedVersion}-{installInfo.clientPlatform}.zip")
    clearScreen()
