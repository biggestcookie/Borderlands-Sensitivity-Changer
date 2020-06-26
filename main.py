import json
import os
import shutil
from typing import Any

from offset import rewrite_sens, get_current_sens, get_current_offset
from profiles import get_profile_path
from util import try_input
from textwrap import dedent

GAMES = ["Borderlands The Pre-Sequel", "Borderlands 2"]
GAME_CHOICE = None
PROFILE_PATH = None
OFFSET = None
CURRENT_SENS = None


def load_config() -> Any:
    config_path = f"{os.path.dirname(os.path.realpath(__file__))}\\config.json"
    try:
        with open(config_path) as config:
            return json.load(config)
    except Exception:
        return


def input_to_game_choice(input: str) -> str:
    choice = int(input)
    return GAMES[choice - 1]


def input_to_menu_choice(input: str) -> bool:
    if input == "1":
        OFFSET = get_current_offset(PROFILE_PATH)
        CURRENT_SENS = get_current_sens(PROFILE_PATH, OFFSET)
        return False
    elif input == "2":
        CURRENT_SENS = rewrite_sens(PROFILE_PATH)
        return False
    else:
        return True


def main():
    menu_prompt = "Type # and press enter: "
    config = load_config()
    text = [
        "Which game are you changing sensitivity for?",
        *[f"{i + 1} - {choice}" for i, choice in enumerate(GAMES)],
    ]
    GAME_CHOICE = try_input(input_to_game_choice, text=text, prompt=menu_prompt)

    save_path = (
        config[GAME_CHOICE]["path"]
        if config and "path" in config[GAME_CHOICE]
        else None
    )
    PROFILE_PATH = get_profile_path(GAME_CHOICE, save_path)

    config[GAME_CHOICE]["path"] = os.path.split(os.path.dirname(PROFILE_PATH))[0]

    print(f"\nBacking up profile.bin to profile.bin.bak", end="\n" * 2)
    shutil.copyfile(PROFILE_PATH, f"{PROFILE_PATH}.bak")

    if config and "offset" in config[GAME_CHOICE]:
        OFFSET = config[GAME_CHOICE]["offset"]
    else:
        OFFSET = get_current_offset(PROFILE_PATH)
    config[GAME_CHOICE]["offset"] = OFFSET

    CURRENT_SENS = get_current_sens(PROFILE_PATH, OFFSET)
    text = [
        dedent(
            f"""
                Current profile path: {PROFILE_PATH}
                Current mouse sensitivity: {CURRENT_SENS}
                If your current sensitivity doesn't look right, try recalculating!
            """
        ),
        "1 - Set mouse sensitivity",
        "2 - Recalculate current sensitivity",
    ]
    menu_choice = False
    while not menu_choice:
        menu_choice = try_input(input_to_menu_choice, text=text, prompt=menu_prompt)


if __name__ == "__main__":
    main()
