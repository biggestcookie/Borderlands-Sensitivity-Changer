import hashlib
import random

from util import try_input


def get_sens_offset(profile_path: str) -> int:
    while True:
        sens_1 = random.randrange(5, 100, 5)
        print(
            f"Please open your game, set your mouse sensitivity to {sens_1}, and exit to main menu."
        )
        input("Press enter once you are done.")

        with open(profile_path, "rb") as f:
            profile_1 = bytearray(f.read()[20:])
            indexes_1 = [i for i, val in enumerate(profile_1) if val == sens_1]

        sens_2 = sens_1
        while sens_2 == sens_1:
            sens_2 = random.randrange(5, 100, 5)

        print(
            f"\nNow set your mouse sensitivity to {sens_2}, and exit to main menu again."
        )
        input("Press enter once you are done.")

        with open(profile_path, "rb") as f:
            profile_2 = bytearray(f.read()[20:])
            indexes_2 = [i for i, val in enumerate(profile_2) if val == sens_2]
        intersection = set(indexes_1).intersection(indexes_2)
        if len(intersection) == 1:
            return intersection.pop()
        print("\nUnable to calculate offset! Restarting.")


def rewrite_sens(profile_path: str):
    offset = get_sens_offset(profile_path)
    sens = try_input(int, "\nEnter your new desired sensitivity (1-255): ")
    with open(profile_path, "rb") as f:
        profile = bytearray(f.read()[20:])
    profile[offset] = sens
    hash = hashlib.sha1()
    hash.update(profile)
    profile[0:0] = bytearray(hash.digest())
    with open(profile_path, "wb") as f:
        f.write(profile)
