import requests


def InstallGame():
    pass

def CheckForUpdates():
    # ChatGPT helped me write this section checking for the latest version

    latestBuildNumber = GetLatestBuildNumber()
    # No more ChatGPT help


def GetLatestBuildNumber():
    Repo = f'https://api.github.com/repos/Lemons-Studios/Mission-Monkey/releases/latest'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(Repo, headers = headers)

    if response.status_code == 200:
        LatestRepoTag = response.json()
        LatestRelease = LatestRepoTag['tag_name']
        return LatestRelease
