import platform
import os

import requests
from tqdm import tqdm
import zipfile
from latestBuild import GetLatestBuildNumber

latestBuildNum = GetLatestBuildNumber("Mission-Monkey")
clientPlatform = platform.system()
gameDirectory = None

# I am too lazy to import from main and whatever so just run the if statement again but instead of the root dir it's the game dir
if platform.system() != "Windows":
    gameDirectory = os.path.join(os.path.expanduser("~"), "Mission-Monkey/Game")
else:
    gameDirectory = os.path.join(os.environ['USERPROFILE'], "/Mission-Monkey/Game")


def installGame():
    # This entire download code was stol- I mean borrowed from StackOverflow (https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests)
    downloadURL = f"https://github.com/Mission-Monkey/releases/{latestBuildNum}/{latestBuildNum}-{clientPlatform}.zip"
    response = requests.get(downloadURL, stream=True)
    totalSize = int(response.headers.get('content-length'), 0)
    blockSize = 1024  # 1 Kilobyte

    progressBar = tqdm(total=totalSize, unit="iB", unit_scale=True)
    with open('game.zip', 'wb') as archivedGame:
        for data in response.iter_content(blockSize):
            progressBar.update(len(data))
            archivedGame.write(data)
    progressBar.close()
    if totalSize != 0 and progressBar.n != totalSize:
        print("Something really bad happened. Try downloading again?")

    try:
        with zipfile.ZipFile(os.path.join(gameDirectory, f'/{latestBuildNum}-{clientPlatform}.zip')) as extractor:
            extractor.extractall()
    except zipfile.BadZipfile:
        print("Error: Downloaded zip file is corrupted, please try again")
