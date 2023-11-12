import requests
import platform, os

def GetLatestBuildNumber(repoName):
    repo = f'https://api.github.com/repos/Lemons-Studios/{repoName}/releases/latest'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(repo, headers=headers)

    if response.status_code == 200:
        latestRepoTag = response.json()
        latestRelease = latestRepoTag['tag_name']
        # print(latestRelease)
        return latestRelease


def clearScreen():
    if platform.system() != 'Windows':
        os.system('clear')
    else:
        os.system('cls')