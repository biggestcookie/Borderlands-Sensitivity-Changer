# Borderlands Sensitivity Changer

### [Download for Windows and Linux+Proton here!](https://github.com/biggestcookie/borderlands-sensitivity-changer/releases/latest)

Borderlands 2 and Borderlands: The Pre-Sequel have a minimum sensitivity value of 10, which [can be frustrating when the minimum sensitivity is still too high](https://www.google.com/search?q=borderlands+2+sensitivity+too+high). This program helps you easily change this value yourself lower than the minimum, or any value of your choosing.

### How does it work?

Your mouse sensitivity is stored in a game settings file called `profile.bin`. The tool finds the exact mouse-sensitivity setting inside that file, changes it to any value you want (1-255, including below the in-game minimum of 10), and writes the file back safely so the game accepts it. Because it edits the setting itself rather than guessing at a position in the file, it works reliably across different accounts and setups.

## Usage

### Installation

The Windows and Linux applications can be found in the [releases](https://github.com/biggestcookie/borderlands-sensitivity-changer/releases) of this repository.

> Before running the tool, launch the game once and change at least one setting so that your `profile.bin` file is created.

#### Windows

Download the Windows application (e.g. `BLSensChanger-Windows.exe`) to any location and run it.

#### Linux

> **Note:** On Linux this tool works only with the Windows version of the game running through Proton, not the Linux-native port.

1. Download the Linux application (e.g. `BLSensChanger-Linux`).
2. Open a terminal and `cd` into the folder your browser saved it to (usually `~/Downloads`).
3. Run `chmod +x ./BLSensChanger-Linux` to make the file executable.
4. Run `./BLSensChanger-Linux` to start the tool.

### Demonstration

```
Which game are you changing sensitivity for?
1 - Borderlands 2
2 - Borderlands The Pre-Sequel

Type # and press enter: 1

To find your active profile: in your game, change mouse sensitivity to a new value and exit to the main menu.
Press enter once you are done.

Active profile: D:\Paul\Documents\My Games\Borderlands 2\WillowGame\SaveData\76561198045674442\profile.bin

Backing up profile.bin to D:\Paul\Documents\My Games\Borderlands 2\WillowGame\SaveData\76561198045674442\profile.bin.bak

Current mouse sensitivity: 35

1 - Set mouse sensitivity
2 - Re-detect active profile
Enter - Quit application

Type # and press enter: 1

Enter your new desired sensitivity (1-255): 5

Done! Restart the game, check the mouse settings, and enjoy your newly configured sensitivity.

WARNING: Next time you launch the game, select your LOCAL save, not the cloud save. If prompted, overwrite the cloud save with your local save.
```

### Alternatives

The 'Uncapped Pause Menu Settings' mod for [Borderlands 2](https://www.nexusmods.com/borderlands2/mods/157) and [The Pre-Sequel](https://www.nexusmods.com/borderlandspresequel/mods/14) allow you to fine-tune your sensitivity, as well as many other settings while in-game, although they require a hex-edit and some prior setup before use.

## Development

### Requirements

[Python 3.10+](https://www.python.org/downloads/)

Install required packages using `pip install -r requirements.txt`

### Building

You can build the program into an executable with the command `pyinstaller main.py --onefile`

## Credits

Linux+Proton support by [@JonLiuFYI](https://github.com/JonLiuFYI).

### References

- [Kaathan's Python script from the Steam BL2 Community](https://steamcommunity.com/app/49520/discussions/0/882960797527726404/#c616188473194554202) - used originally as a reference for this program
- [`swimmesberger/bo2-profile-editor`](https://github.com/swimmesberger/bo2-profile-editor) - documents the `profile.bin` structure and provided reference data used to validate the decoder.
- [`lzokay`](https://pypi.org/project/lzokay/) - the LZO compression library used to read and write `profile.bin`.

## Disclaimer

This tool and the reverse-engineered `profile.bin` solution were created with AI assistance. The original solution was written manually, and the current solution was tested manually.
