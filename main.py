import shutil
from textwrap import dedent

from config import CONFIG
from offset import calculate_offset, get_current_sens, rewrite_sens
from profiles import get_profile_path


def main():
    profile_path = get_profile_path()
    print("\nBacking up profile.bin to profile.bin.bak")
    shutil.copyfile(profile_path, f"{profile_path}.bak")

    offset: int = CONFIG.get_data("offset")
    if offset is None:
        offset = calculate_offset(profile_path)
    current_sens: int = get_current_sens(profile_path, offset)

    choice_prompts = [
        "1 - Set mouse sensitivity",
        "2 - Recalculate current sensitivity",
        "Enter - Quit application",
    ]

    while True:
        print(
            dedent(
                f"""
                    Current mouse sensitivity: {current_sens}
                    If your current sensitivity doesn't look right, try recalculating!
                """
            )
        )
        print(*choice_prompts, sep="\n", end="\n" * 2)
        choice = input("Type # and press enter: ")
        if choice == "1":
            current_sens = rewrite_sens(profile_path, offset)
        elif choice == "2":
            offset = calculate_offset(profile_path)
            current_sens = get_current_sens(profile_path, offset)
        elif choice == "":
            print("Exiting.", end="\n" * 2)
            break
        else:
            print("Not a valid choice.")


if __name__ == "__main__":
    main()
