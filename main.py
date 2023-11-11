from mainMenu import menu
import platform
import os
from latestBuild import GetLatestBuildNumber

gameDirectory = './build'
buildInfo = f'{gameDirectory}/buildInfo.txt'


def firstLaunch():
    os.mkdir(gameDirectory)
    with open(buildInfo, 'w') as latestBuild:
        latestBuild.write(GetLatestBuildNumber("Mission-Monkey"))
    # Will be uncommented after testing
    # match platform.system():
    #    case 'Windows':
    #        pass
    #    case 'Darwin':  # MacOS
    #        pass
    #    case 'Linux':
    #        pass


if not os.path.exists(gameDirectory) or not os.path.exists(buildInfo):
    firstLaunch()

menu()
