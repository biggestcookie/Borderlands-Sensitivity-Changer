# Borderlands Sensitivity Changer

### [Download it here!](https://github.com/biggestcookie/borderlands-sensitivity-changer/releases/latest)

Borderlands 2 and Borderlands: The Pre-Sequel have a minimum sensitivity value of 10, which [can be frustrating when the minimum sensitivity is still too high](https://www.google.com/search?q=borderlands+2+sensitivity+too+high). This program helps you easily change this value yourself lower than the minimum, or any value of your choosing.

### How does it work?

Your mouse sensitivity, among other user settings, are stored somewhere in a file called `profile.bin`. This setting is stored in a location that seems to vary from user to user. During the calculation, the tool asks you to set your mouse sensitivity to different values, calculates the hex offset of each of these values, and attempts to find where these offsets overlap. This offset is saved and used when you want to set your own custom mouse sensitivity, which can be any number between 1 - 255.

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

Please open your game, set your mouse sensitivity to 50, and exit to main menu.
Press enter once you are done.

Now set your mouse sensitivity to 75, and exit to main menu again.
Press enter once you are done.

Calculated successfully!

Current mouse sensitivity: 75
If your current sensitivity doesn't look right, try recalculating!

1 - Set mouse sensitivity
2 - Recalculate current sensitivity
Enter - Quit application

Type # and press enter: 1

Enter your new desired sensitivity (1-255): 2

Done! Restart the game, check the mouse settings, and enjoy your newly configured sensitivity.
```

### Alternatives

The 'Uncapped Pause Menu Settings' mod for [Borderlands 2](https://www.nexusmods.com/borderlands2/mods/157) and [The Pre-Sequel](https://www.nexusmods.com/borderlandspresequel/mods/14) allow you to fine-tune your sensitivity, as well as many other settings while in-game, although they require a hex-edit and some prior setup before use.

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
