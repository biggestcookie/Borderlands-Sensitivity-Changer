import os
from pathlib import Path

from config import CONFIG
from exceptions import SaveDataNotFound
from util import try_input
from user_os import UserOS


def input_to_game_path(input: str) -> str:
    save_path = Path(input) / "SaveData"
    if save_path.is_dir():
        CONFIG.set_data("path", str(save_path))
        profile_path: Path = get_latest_directory(save_path) / "profile.bin"
        if profile_path.is_file():
            return str(profile_path)
    raise Exception("profile.bin not found in given path.")


def get_latest_directory(path: Path | None) -> Path:
    """Return the most recently modified folder within `path`.

    Exceptions that may bubble up:
    * FileNotFoundError
    * TypeError - `path` is None, has no subdirectories, or doesn't exist"""
    if path is None:
        raise TypeError

    subdirs = filter(lambda p: p.is_dir(), path.iterdir())
    return max(subdirs, key=lambda p: p.stat().st_mtime)


def get_profile_path(user_os: UserOS) -> str | Path:
    save_path_init: str | None = CONFIG.get_data("path")
    if save_path_init is not None:
        save_path = Path(save_path_init)
    else:
        try:
            save_path = user_os.find_savedata()
        except SaveDataNotFound as errpath:
            save_path = None
            print(
                "It seems like your SaveData folder isn't in the usual location. ",
                errpath,
            )
        else:
            CONFIG.set_data("path", str(save_path))

    # Sentinel value that almost certainly isn't valid a valid Path on a normal
    # person's PC. This is extremely cursed and hacky. (Linear A Sign A661)
    profile_path = Path("𐜳")
    try:
        latest_subdir = get_latest_directory(save_path)
        profile_path = Path(latest_subdir) / "profile.bin"
    except (TypeError, FileNotFoundError):
        if not profile_path.is_file():
            profile_path = try_input(
                input_to_game_path,
                text=user_os.savedata_not_found,
                error=f"Couldn't find WillowGame at that path. Please try entering your path again: ",
            )

    print(f"\nFound latest profile.bin at {profile_path}")
    return profile_path
