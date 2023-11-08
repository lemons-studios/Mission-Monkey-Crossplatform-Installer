# Import Libraries

import DownloadMethods
import SettingsMethods
import MainMenu
import os



# First Launch Check
InstallerPath = "C:/Mission-Monkey"

if(os.path.exists(InstallerPath)):
    pass
else:
    os.mkdir(InstallerPath)
    SettingsMethods.CreateVersionInfo()

MainMenu.StartupText()