import os
import platform

import mainMenu
from latestBuild import GetLatestBuildNumber
from installAndUpdateGame import InstallationInformation

installInfo = InstallationInformation()

def firstLaunch():
    os.mkdir(installInfo.gameDirectory)
    with open(installInfo.buildInfo, 'w') as latestBuild:
        latestBuild.write(GetLatestBuildNumber("Mission-Monkey"))


if not os.path.exists(installInfo.gameDirectory) or not os.path.exists(installInfo.buildInfo):
    firstLaunch()

mainMenu.menu()
