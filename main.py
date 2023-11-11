from mainMenu import menu
import platform
import os
from latestBuild import GetLatestBuildNumber

if platform.system() != "Windows":
    gameRootDir = os.path.join(os.path.expanduser("~"), "/Mission-Monkey")
else:
    gameRootDir = os.path.join(os.environ['USERPROFILE'], "./Mission-Monkey")  # This Environment thing was made by the GPT man

buildInfo = f'{gameRootDir}/buildInfo.txt'


def firstLaunch():
    os.mkdir(gameRootDir)
    with open(buildInfo, 'w') as latestBuild:
        latestBuild.write(GetLatestBuildNumber("Mission-Monkey"))


if not os.path.exists(gameRootDir) or not os.path.exists(buildInfo):
    firstLaunch()

menu()
