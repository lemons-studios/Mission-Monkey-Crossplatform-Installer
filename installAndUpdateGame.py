import platform
import os
import shutil
import requests

from tqdm import tqdm
from latestBuild import GetLatestBuildNumber, clearScreen


class InstallationInformation:
    latestBuildNum = GetLatestBuildNumber("Mission-Monkey")
    clientPlatform = platform.system()
    gameDirectory = None
    gameData = None

    if platform.system() != "Windows":
        gameData = os.path.join(os.environ['USERPROFILE'], "Mission-Monkey", "game.zip")
        gameDirectory = os.path.join(os.path.expanduser("~"), "Mission-Monkey")
    else:
        gameDirectory = os.path.join(os.environ['USERPROFILE'], "Mission-Monkey")
        gameData = os.path.join(os.path.expanduser("~"), "Mission-Monkey", "game.zip")

    buildInfo = f'{gameDirectory}/buildInfo.txt'
    downloadURL = f"https://github.com/lemons-studios/Mission-Monkey/releases/download/{latestBuildNum}/{latestBuildNum}-{clientPlatform}.zip"


installInfo = InstallationInformation()


def installGame():
    # Part of this download code was borrowed from StackOverflow (https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests)

    response = requests.get(installInfo.downloadURL, stream=True)
    totalSize = int(response.headers.get('content-length'), 0)
    blockSize = 1024  # 1 Kilobyte
    progressBar = tqdm(total=totalSize, unit="iB", unit_scale=True)
    with open(os.path.join(installInfo.gameDirectory, "game.zip"), 'wb') as archivedGame:
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
    # TODO: make a prompt asking the user what to do after the install is done
    clearScreen()
    return


def updateGame():
    # TODO: make a prompt asking the user what to do after the update is done
    installedBuild = open(f'{installInfo.gameDirectory}/buildInfo.txt').readline()
    if installedBuild != installInfo.latestBuildNum:
        print(f"There is a new version available ({installInfo.latestBuildNum})! ")

    else:
        print("You have the latest version of Mission: Monkey installed on your computer")



def repairInstallation():
    # Delete any files in the installation directory (except for the build info file), and call the installGame method after to download the new version of the game
    # TODO: make a prompt asking the user what to do after the reinstall is done
    clearScreen()

