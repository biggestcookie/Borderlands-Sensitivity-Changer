# Borderlands Sensitivity Changer
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W71USFG)

Borderlands 2 and Borderlands: The Pre-Sequel allow you to change mouse sensitivity only in increments of 10. Unfortunately you cannot fine-tune this value yourself or set this value below 10, which [can be frustrating](https://www.google.com/search?q=borderlands+2+sensitivity+too+high). This application helps you easily change this value yourself by walking you through a simple automated process, where it calculates the hex offset of your mouse sensitivity in your save file and edits it for you.

## Usage

### Releases

The built application can be found in the [releases](https://github.com/biggestcookie/borderlands-sens-changer/releases) of this repository. Simply download the application to any location and run it.

Currently there is only Windows support.

### Demonstration

```
Which game are you changing sensitivity for?
1 - BORDERLANDS_PRESEQUEL
2 - BORDERLANDS_2
Type # and press enter: 2

Backing up profile.bin to profile.bin.bak

Please open your game, set your mouse sensitivity to 95, and exit to main menu.
Press enter once you are done.

Now set your mouse sensitivity to 60, and exit to main menu again.
Press enter once you are done.

Enter your new desired sensitivity (1-255): 3

Done! Restart the game, check the mouse settings, and enjoy your newly configured sensitivity.
If this did not work for you, rename profile.bin.bak to profile.bin (replacing the current one), found at D:\Users\Paul\Documents\My Games\Borderlands 2\WillowGame\SaveData\76561198045674442
```

## Development

### Requirements

[Python 3.5+](https://www.python.org/downloads/)

Install required packages using `pip install -r requirements.txt`

### Building

You can build the application into an executable with the command `pyinstaller main.py --onefile`

## Credits

This script is an improved version of a solution found on the [Borderlands 2 Steam Community](https://steamcommunity.com/app/49520/discussions/0/882960797527726404/) by user [Kaathan](https://steamcommunity.com/id/Kaathan).
