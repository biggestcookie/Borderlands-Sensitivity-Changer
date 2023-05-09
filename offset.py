import hashlib
from pathlib import Path
import random

from config import CONFIG
from util import try_input


def calculate_offset(profile_path: str | Path) -> int:
    while True:
        complete_prompt = "Press enter once you are done. "
        sens_1 = random.randrange(10, 100, 5)
        print(
            f"\nPlease open your game, set your mouse sensitivity to {sens_1}, and exit to main menu."
        )
        input(complete_prompt)

        with open(profile_path, "rb") as f:
            profile_1 = bytearray(f.read()[20:])
            indexes_1 = [i for i, val in enumerate(profile_1) if val == sens_1]

        sens_2 = sens_1
        while sens_2 == sens_1:
            sens_2 = random.randrange(10, 100, 5)

        print(
            f"\nNow set your mouse sensitivity to {sens_2}, and exit to main menu again."
        )
        input(complete_prompt)

        with open(profile_path, "rb") as f:
            profile_2 = bytearray(f.read()[20:])
            indexes_2 = [i for i, val in enumerate(profile_2) if val == sens_2]
        intersection = set(indexes_1).intersection(indexes_2)
        if len(intersection) == 1:
            offset = intersection.pop()
            CONFIG.set_data("offset", offset)
            print("\nCalculated successfully!")
            return offset
        print("\nUnable to calculate offset! Restarting.")


def get_current_sens(profile_path: str | Path, offset: int) -> int:
    with open(profile_path, "rb") as f:
        profile = bytearray(f.read()[20:])
        return profile[offset]


def rewrite_sens(profile_path: str | Path, offset) -> int:
    sens = try_input(int, prompt="\nEnter your new desired sensitivity (1-255): ")
    with open(profile_path, "rb") as f:
        profile = bytearray(f.read()[20:])
    profile[offset] = sens
    hash = hashlib.sha1()
    hash.update(profile)
    profile[0:0] = bytearray(hash.digest())
    with open(profile_path, "wb") as f:
        f.write(profile)
    print(
        "\nDone! Restart the game, check the mouse settings, and enjoy your newly configured sensitivity."
    )
    return sens
