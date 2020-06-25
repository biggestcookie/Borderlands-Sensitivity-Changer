from ctypes import windll
from enum import Enum
import os
import string
from typing import List

from util import try_input


class GameChoice(Enum):
    BORDERLANDS_PRESEQUEL = 1
    BORDERLANDS_2 = 2


def input_to_game_choice(input: str) -> str:
    choice = GameChoice(int(input))
    if choice == GameChoice.BORDERLANDS_PRESEQUEL:
        return "Borderlands The Pre-Sequel"
    else:
        return "Borderlands 2"


def input_to_game_path(input: str) -> str:
    save_path = f"{input}\\SaveData\\"
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
    print("Which game are you changing sensitivity for?")
    print(*[f"{choice.value} - {choice.name}" for choice in GameChoice], sep="\n")
    game_choice = try_input(input_to_game_choice, "Type # and press enter: ")

    path = "{0}:\\Users\\{1}\\Documents\\My Games\\{2}\\WillowGame\\SaveData\\"
    user = os.environ["USERNAME"]

    profile_path = ""
    for drive in get_drives():
        save_path = path.format(drive, user, game_choice)
        if os.path.exists(save_path):
            profile_path = f"{get_latest_directory(save_path)}\\profile.bin"

    if not os.path.isfile(profile_path):
        print(f"\nCould not find '{game_choice}\\WillowGame\\SaveData'.")
        print(
            f"Please enter the path to WillowGame, ex: C:\\Users\\CL4P-TP\\Documents\\My Games\\{game_choice}\\WillowGame"
        )
        profile_path = try_input(
            input_to_game_path, error=f"Couldn't find WillowGame at that path."
        )
    return profile_path
