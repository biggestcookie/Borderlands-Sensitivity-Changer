from ctypes import windll
import os
import string
from typing import List

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
    drives: List[str] = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


def get_latest_directory(path: str) -> str:
    return max([os.path.join(path, d) for d in os.listdir(path)], key=os.path.getmtime,)


def get_profile_path() -> str:
    save_path = CONFIG.get_data("path")
    game_choice = CONFIG.game_choice.value

    profile_path = ""
    if not save_path:
        path = "{0}:\\Users\\{1}\\Documents\\My Games\\{2}\\WillowGame\\SaveData\\"
        user = os.environ["USERNAME"]
        for drive in get_drives():
            save_path = path.format(drive, user, game_choice)
            if os.path.exists(save_path):
                CONFIG.set_data("path", save_path)
                break
    try:
        profile_path = f"{get_latest_directory(save_path)}\\profile.bin"
    except FileNotFoundError:
        if not os.path.isfile(profile_path):
            text = [
                f"\nCould not find '{game_choice}\\WillowGame\\SaveData'.",
                f"Please enter the full path to WillowGame, this can usually be found in 'Documents\\My Games\\{game_choice}'.",
                f"Ex. C:\\Users\\CL4P-TP\\Documents\\My Games\\{game_choice}\\WillowGame",
            ]
            profile_path = try_input(
                input_to_game_path,
                text=text,
                error=f"Couldn't find WillowGame at that path. Please try entering your path again: ",
            )
    print(f"\nFound latest profile.bin at {profile_path}")
    return profile_path
