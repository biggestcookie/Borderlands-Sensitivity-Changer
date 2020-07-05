# Borderlands Sensitivity Changer

Borderlands 2 and Borderlands: The Pre-Sequel allow you to change mouse sensitivity only in increments of 10. Unfortunately you cannot fine-tune this value yourself or set this value below 10, which [can be frustrating](https://www.google.com/search?q=borderlands+2+sensitivity+too+high). This program helps you easily change this value yourself by walking you through a simple automated process, where it calculates the hex offset of your mouse sensitivity in your save file and edits it for you.

## Usage

### Releases

The built application can be found in the [releases](https://github.com/biggestcookie/borderlands-sensitivity-changer/releases) of this repository. Simply download the application to any location and run it. Make sure you have run the game and have changed some settings at least once before launching.

Currently there is only Windows support.

### Demonstration

```
Which game are you changing sensitivity for?
1 - Borderlands 2
2 - Borderlands The Pre-Sequel

Type # and press enter: 1

Found latest profile.bin at D:\Paul\Documents\My Games\Borderlands 2\WillowGame\SaveData\76561198045674442\profile.bin

Backing up profile.bin to profile.bin.bak

Current mouse sensitivity: 3
If your current sensitivity doesn't look right, try recalculating!

1 - Set mouse sensitivity
2 - Recalculate current sensitivity
Enter - Quit application

Type # and press enter:
```

## Development

### Requirements

[Python 3.5+](https://www.python.org/downloads/)

Install required packages using `pip install -r requirements.txt`

### Building

You can build the program into an executable with the command `pyinstaller main.py --onefile`

## Credits

This program is an improvement of a solution found on the [Borderlands 2 Steam Community](https://steamcommunity.com/app/49520/discussions/0/882960797527726404/#c616188473194554202) by user Kaathan.

---

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W71USFG)
