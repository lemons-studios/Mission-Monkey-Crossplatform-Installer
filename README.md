# Mission: Monkey Cross-Platform CLI installer

This is a simple Python application that installs the latest build of "Mission: Monkey" onto your computer

## Supported Operating Systems
- Windows 8 or newer
- MacOS (Darwin) 10.15 (Catalina) or newer
- Any modern Linux distribution
  
> **Note**  
> This installer supports versions above 0.3 and above, as it is the first crossplatform release

## How to use
Simply download the latest release and open it! (either from a terminal or from your file explorer)

**It is strongly recommended to run this application in a maximized console window**

## Development Requirements
- [Python 3](https://www.python.org/downloads/) [With Pip](https://pip.pypa.io/en/stable/installation/#get-pip-py)
- [PyCharm (Recommended)](https://www.jetbrains.com/pycharm/)
- Install 3rd Party libraries & pipenv
    ```sh
    pip install asdf pipenv
    pip install -r requirements.txt
    ```
- Create new pipenv environment or let pycharm make it for you
  ```sh
  cd MissionMonkeyInstaller-Cli
  pipenv install
  ```
  > **Note**
  > This application only runs in the command prompt/consoles of operating systems, not in any IDE consoles
