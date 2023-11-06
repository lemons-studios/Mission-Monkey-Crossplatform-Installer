# Import Libraries

from tqdm import tqdm
import requests


class MenuFunctions:
    def StartupText(self):
        print("Welcome to the Mission: Monkey CLI installer!")
        print("Select what you want to do:")
        print("")

    def SettingsMenu(self):
        print("Settings Menu")

class DownloadMethods:

    def InstallGame(self):

        print("Temp")

    def CheckForUpdates(self):
        # ChatGPT helped me write this section checking for the latest version
        Repo = f'https://api.github.com/repos/Lemons-Studios/Mission-Monkey/releases/latest'
        headers = {'Accept': 'application/vnd.github.v3+json'}

        response = requests.get(Repo, headers = headers)

        if response.status_code == 200:
            LatestRepoTag = response.json()
            LatestRelease = LatestRepoTag['tag_name']
            print(LatestRelease)
        # No more ChatGPT help


DownloadFunctions = DownloadMethods()

DownloadFunctions.CheckForUpdates()