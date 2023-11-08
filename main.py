# Import Libraries

import DownloadMethods
import SettingsMethods
import MainMenu
import os
import GlobalVariables

# First Launch Check
InstallerPath = "./Mission-Monkey"

if(os.path.exists(InstallerPath)):
    pass
else:
    os.mkdir(InstallerPath)
    open(GlobalVariables.InstallBuildFile)

SettingsMethods.CreateVersionInfo()