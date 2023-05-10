import os
from pathlib import Path

from config import CONFIG
from util import try_input
from user_os import UserOS


def input_to_game_path(input: str) -> str:
    save_path = f"{input}\\SaveData\\"
    if os.path.isdir(save_path):
        CONFIG.set_data("path", save_path)
        profile_path = f"{get_latest_directory(save_path)}\\profile.bin"
        if os.path.isfile(profile_path):
            return profile_path
    raise Exception("profile.bin not found in given path.")


def get_latest_directory(path: str) -> str:
    return max(
        [os.path.join(path, d) for d in os.listdir(path)],
        key=os.path.getmtime,
    )


def get_profile_path(user_os: UserOS) -> str | Path:
    save_path: str | None = CONFIG.get_data("path")

    profile_path = ""
    if save_path is None:
        save_path = user_os.find_savedata()
        if save_path is not None:
            CONFIG.set_data("path", save_path)

    try:
        profile_path = Path(get_latest_directory(save_path)) / "profile.bin"  # type: ignore - save_path is no longer None by now
    except FileNotFoundError:
        if not os.path.isfile(profile_path):
            profile_path = try_input(
                input_to_game_path,
                text=user_os.savedata_not_found,
                error=f"Couldn't find WillowGame at that path. Please try entering your path again: ",
            )
    print(f"\nFound latest profile.bin at {profile_path}")
    return profile_path
