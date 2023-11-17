<img src="https://cdn.discordapp.com/attachments/1154895197470208112/1174221553681039441/MissionMonkeyInstallerIcon.png?ex=6566ce0a&is=6554590a&hm=20963ecdc0340e1d26f533f4c96849382829cb2da9ece39c9c42fb0e93e9fa9b&">

# Mission: Monkey Cross-Platform CLI installer

This is a simple Python application that installs the latest build of "Mission: Monkey" onto your computer

## 💻 Supported Operating Systems
- Windows 8 or newer
- MacOS (Darwin) 10.15 (Catalina) or newer
- Any modern Linux distribution
  
> **Note**
> This installer supports versions above 0.3 and above, as it is the first crossplatform release

## 🚀 How to use
### 🪟Windows
- Simply just open the executable!

### 🐧Linux & 🍎 MacOS
- Download the file
- Make the file executable
  - You can either do this in your desktop environment or run the following command into your terminal (assuming that the terminal is in the directory the executable is found in:
    ```sh
    chmod 777 ./MissionMonkeyInstaller-{OperatingSystemHere} 
    ```
    > **Note**
    > You can hit the tab key while typing in the terminal for the filename/command to autocomplete
    
**It is strongly recommended to run this application in a maximized console window**


## 🛠️ Development Requirements
- [Python 3.8 or higher](https://www.python.org/downloads/) [With Pip](https://pip.pypa.io/en/stable/installation/#get-pip-py)
- [PyCharm (Recommended)](https://www.jetbrains.com/pycharm/)
- Install 3rd Party libraries & pipenv (asdf is a runtime dependency for pipenv)
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


## 🏗️ Build from source
> **Note**
> You must have Python 3.8 with pip to be able to build from source
 
Run the following commands to build from source:

```sh
git clone https://github.com/lemons-studios/MissionMonkeyInstaller-cli.git
cd MissionMonkeyInstaller-cli
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile --icon=MissionMonkeyInstallerIcon.ico src/main.py
```

final builds are located in dist/
