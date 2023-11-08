import DownloadMethods

def CreateVersionInfo():
    with open(r'C:/MissionMonkey/buildinfo.txt', 'w') as buildInfo:
        buildInfo.write(DownloadMethods.GetLatestBuildNumber())
