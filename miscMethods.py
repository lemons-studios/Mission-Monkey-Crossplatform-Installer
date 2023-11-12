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

class MenuStyes:
    AcceptedASCIIFonts = \
        [
            "3-d", "64f1", "6x10", "6x9", "advenger", "amcaa01",
            "alphabet", "amcrazo2", "amcrazor", "amcslash", "amctubes",
            "amcun1", "aquaplan", "arrows", "asc", "avatar", "barbwire", "basic",
            "bell", "big", "bigfig", "bolger", "braced", "bulbhead", "char4", "charact3",
            "charact4", "chunky", "clr6x6", "coinstak", "cola", "colossal", "computer", "contrast",
            "crawford", "cricket", "cybermedium", "dietcola", "doom", "double", "drpepper", "druid",
            "eftifont", "eftirobot", "eftiwater", "epic", "fantasy", "filter", "fire_font-s", "flipped",
            "future_4", "future_6", "future_8", "graffiti", "greek", "henry3d", "jacky", "jazmine", "katakana",
            "letters", "lineblocks", "modular", "nancyj", "nancyj-fancy", "ogre", "os2", "pawp", "peaks",
            "puffy", "rectangles", "red_phoenix", "rounded", "script", "serifcap", "slant", "small",
            "smallcaps", "smkeyboard", "smpoison", "smslant", "soft", "standard", "starwars", "stforek",
            "thin", "tinker-toy", "tubular", "unarmed", "utopia", "xtimes"
        ]
