import platform
import os

import requests
from tqdm import tqdm
from clear_screen import clear
import shutil
from latestBuild import GetLatestBuildNumber

latestBuildNum = GetLatestBuildNumber("Mission-Monkey")
clientPlatform = platform.system()
gameDirectory = None

# I am too lazy to import from main and whatever so just run the if statement again but instead of the root dir it's the game dir
if platform.system() != "Windows":
    gameDirectory = os.path.join(os.path.expanduser("~"), "Mission-Monkey")
else:
    gameDirectory = os.path.join(os.environ['USERPROFILE'], "Mission-Monkey")


def installGame():
    # Part of this download code was borrowed from StackOverflow (https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests)
    downloadURL = f"https://github.com/lemons-studios/Mission-Monkey/releases/download/{latestBuildNum}/{latestBuildNum}-{clientPlatform}.zip"
    response = requests.get(downloadURL, stream=True)
    totalSize = int(response.headers.get('content-length'), 0)
    blockSize = 1024  # 1 Kilobyte

    progressBar = tqdm(total=totalSize, unit="iB", unit_scale=True)
    with open(os.path.join(gameDirectory, "game.zip"), 'wb') as archivedGame:
        for data in response.iter_content(blockSize):
            progressBar.update(len(data))
            archivedGame.write(data)
    progressBar.close()
    if totalSize != 0 and progressBar.n != totalSize:
        print("Something terrible happened. Try downloading again?")

    print("Extracing game")
    gameData = None
    if platform.system() != 'Windows':
        gameData = os.path.join(os.environ['USERPROFILE'], "Mission-Monkey", "game.zip")
        pass
    else:
        gameData = os.path.join(os.path.expanduser("~"), "Mission-Monkey", "game.zip")
        pass
    shutil.unpack_archive(gameData, gameDirectory)
    os.remove(gameData)  # Delete the game zip archive after downloading
    clear()
