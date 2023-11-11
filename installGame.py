import platform
import os



def installGameHandler():
    match platform.system():
        case 'Windows':
            installGame_Windows()
        case 'Linux':
            installGame_Linux()
        case 'Darwin':  # MacOS
            installGame_Darwin()


def installGame_Windows():
    pass


def installGame_Linux():
    pass


def installGame_Darwin():
    pass
