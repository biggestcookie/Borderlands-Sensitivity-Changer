"""Platform-specific behaviors that must be implemented for each supported OS"""

from abc import ABC, abstractmethod
import os
from pathlib import Path

from exceptions import SaveDataNotFound
from game_choice import Game_Choice


class UserOS(ABC):
    """Base class for platform-specific things needed to find profile.bin"""

    def __init__(self, game_choice: Game_Choice) -> None:
        self.game: str = game_choice.value

    @property
    @abstractmethod
    def savedata_not_found(self) -> list[str]:
        """Error message if the path to SaveData wasn't found"""
        pass

    @abstractmethod
    def find_savedata(self) -> Path:
        """Return an absolute path to the chosen game's default SaveData folder
        (where profile.bin is), or raise an exception if it wasn't found.

        Exceptions:
        * SaveDataNotFound - The SaveData folder doesn't exist at its default location.
        """
        pass


class Linux(UserOS):
    def __init__(self, game_choice: Game_Choice) -> None:
        super().__init__(game_choice)
        steam_ids = {
            "Borderlands 2": "49520",
            "Borderlands The Pre-Sequel": "261640",
        }
        self._steamid = steam_ids[self.game]
        self._errmsg = [
            f"\nCould not find '{self.game}/WillowGame/SaveData' for the Proton version of {self.game}.",
            f"Please enter the full path to WillowGame, this can usually be found in",
            f"'steamapps/compatdata/{self._steamid}/pfx/drive_c/users/steamuser/Documents/My Games/{self.game}'.",
            f"                     ({'^' * len(self._steamid)} the Steam ID of {self.game})",
            f"Ex. /home/CL4P-TP/.steam/steam/steamapps/...<ETC>.../{self.game}/WillowGame",
        ]

    @property
    def savedata_not_found(self) -> list[str]:
        return self._errmsg

    def find_savedata(self) -> Path:
        save_path = (
            Path.home()
            / f".steam/steam/steamapps/compatdata/{self._steamid}/pfx/drive_c/users/steamuser/Documents/My Games/{self.game}/WillowGame/SaveData/"
        )
        if not save_path.exists():
            raise SaveDataNotFound(str(save_path))
        return save_path


class Windows(UserOS):
    def __init__(self, game_choice: Game_Choice) -> None:
        super().__init__(game_choice)
        self._errmsg = [
            f"\nCould not find '{self.game}\\WillowGame\\SaveData'.",
            f"Please enter the full path to WillowGame, this can usually be found in 'Documents\\My Games\\{self.game}'.",
            f"Ex. C:\\Users\\CL4P-TP\\Documents\\My Games\\{self.game}\\WillowGame",
        ]

    @staticmethod
    def get_drives() -> list[str]:
        from ctypes import windll  # type: ignore
        import string

        drives: list[str] = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1
        return drives

    @property
    def savedata_not_found(self) -> list[str]:
        return self._errmsg

    def find_savedata(self) -> Path:
        user = os.environ["USERNAME"]
        for drive in self.get_drives():
            save_path = (
                Path(f"{drive}:/Users")
                / f"{user}/Documents/My Games/{self.game}/WillowGame/SaveData"
            )
            if os.path.exists(save_path):
                return save_path

        raise SaveDataNotFound
