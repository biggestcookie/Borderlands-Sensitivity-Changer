import os
import shutil

from offset import rewrite_sens
from profiles import get_profile_path


def main():
    profile_path = get_profile_path()
    print(f"\nBacking up profile.bin to profile.bin.bak", end="\n" * 2)
    shutil.copyfile(profile_path, f"{profile_path}.bak")
    rewrite_sens(profile_path)
    print(
        "\nDone! Restart the game, check the mouse settings, and enjoy your newly configured sensitivity."
    )
    print(
        f"If this did not work for you, rename profile.bin.bak to profile.bin (replacing the current one), found at {os.path.dirname(profile_path)}",
        end="\n" * 2,
    )
    input("Press enter to exit.")


if __name__ == "__main__":
    main()
