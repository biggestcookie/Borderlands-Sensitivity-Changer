import os
from pathlib import Path  # to get linux home dir
import platform
import string
from typing import List

if platform.system() == "Windows":
    from ctypes import windll  # type: ignore

from config import CONFIG
from util import try_input


def input_to_game_path(input: str) -> str:
    save_path = f"{input}\\SaveData\\"
    if os.path.isdir(save_path):
        CONFIG.set_data("path", save_path)
        profile_path = f"{get_latest_directory(save_path)}\\profile.bin"
        if os.path.isfile(profile_path):
            return profile_path
    raise Exception("profile.bin not found in given path.")


def get_drives() -> List[str]:
    """Windows-only"""
    drives: List[str] = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


def get_latest_directory(path: str) -> str:
    return max(
        [os.path.join(path, d) for d in os.listdir(path)],
        key=os.path.getmtime,
    )


def get_profile_path() -> str | Path:
    save_path: str | None = CONFIG.get_data("path")
    game_choice = CONFIG.game_choice.value

    # linux-specific values
    steam_ids = {
        "Borderlands 2": "49520",
        "Borderlands The Pre-Sequel": "261640",
    }
    id = steam_ids[game_choice]

    profile_path = ""
    if not save_path:
        if platform.system() == "Windows":
            path = "{0}:\\Users\\{1}\\Documents\\My Games\\{2}\\WillowGame\\SaveData\\"
            user = os.environ["USERNAME"]
            for drive in get_drives():
                save_path = path.format(drive, user, game_choice)
                if os.path.exists(save_path):
                    CONFIG.set_data("path", save_path)
                    break
        if platform.system() == "Linux":
            save_path = f"{Path.home()}/.steam/steam/steamapps/compatdata/{id}/pfx/drive_c/users/steamuser/Documents/My Games/{game_choice}/WillowGame/SaveData/"
            if Path(save_path).exists():
                CONFIG.set_data("path", save_path)

    try:
        profile_path = Path(get_latest_directory(save_path)) / "profile.bin"  # type: ignore - save_path is no longer None by now
    except FileNotFoundError:
        if not os.path.isfile(profile_path):
            err_windows = [
                f"\nCould not find '{game_choice}\\WillowGame\\SaveData'.",
                f"Please enter the full path to WillowGame, this can usually be found in 'Documents\\My Games\\{game_choice}'.",
                f"Ex. C:\\Users\\CL4P-TP\\Documents\\My Games\\{game_choice}\\WillowGame",
            ]
            err_linux = [
                f"\nCould not find '{game_choice}/WillowGame/SaveData' for the Proton version of {game_choice}.",
                f"Please enter the full path to WillowGame, this can usually be found in",
                f"'steamapps/compatdata/{id}/pfx/drive_c/users/steamuser/Documents/My Games/{game_choice}'.",
                f"                     ({'^' * len(id)} the Steam ID of {game_choice})",
                f"Ex. /home/CL4P-TP/.steam/steam/steamapps/ <...> /{game_choice}/WillowGame",
            ]

            text = err_windows if platform.system == "Windows" else err_linux
            profile_path = try_input(
                input_to_game_path,
                text=text,
                error=f"Couldn't find WillowGame at that path. Please try entering your path again: ",
            )
    print(f"\nFound latest profile.bin at {profile_path}")
    return profile_path
