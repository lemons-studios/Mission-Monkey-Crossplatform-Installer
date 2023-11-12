import os
import platform

import mainMenu
from miscMethods import GetLatestBuildNumber, clearScreen
from installAndUpdateGame import InstallationInformation

installInfo = InstallationInformation()

# I would have LOVED to move this to miscMethods, but the moment i did, the entire project decided to kill itself, so these files remain here forever now I guess
def firstLaunch():
    os.mkdir(installInfo.gameDirectory)
    with open(installInfo.buildInfo, 'w') as latestBuild:
        latestBuild.write(GetLatestBuildNumber("Mission-Monkey"))


if not os.path.exists(installInfo.gameDirectory) or not os.path.exists(installInfo.buildInfo):
    firstLaunch()

clearScreen()
mainMenu.menu()
