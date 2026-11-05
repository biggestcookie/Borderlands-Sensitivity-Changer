import shutil
from textwrap import dedent

from config import CONFIG
from profiles import get_profile_path
from sensitivity import find_active_profile, read_sens, write_sens


def main():
    profile_path = get_profile_path(CONFIG.user_os)
    active = find_active_profile(profile_path)
    print(f"\nBacking up profile.bin to {active}.bak")
    shutil.copyfile(active, f"{active}.bak")

    current_sens: int = read_sens(active)

    choice_prompts = [
        "1 - Set mouse sensitivity",
        "2 - Re-detect active profile",
        "Enter - Quit application",
    ]

    while True:
        print(
            dedent(
                f"""
                    Current mouse sensitivity: {current_sens}
                """
            )
        )
        print(*choice_prompts, sep="\n", end="\n" * 2)
        choice = input("Type # and press enter: ")
        if choice == "1":
            current_sens = write_sens(active)
        elif choice == "2":
            active = find_active_profile(profile_path)
            current_sens = read_sens(active)
        elif choice == "":
            print("Exiting.", end="\n" * 2)
            break
        else:
            print("Not a valid choice.")


if __name__ == "__main__":
    main()
