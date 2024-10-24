import json
from pathlib import Path
import platform
import sys
from typing import Any

import __main__
from game_choice import Game_Choice
import user_os
from util import try_input


class Config:
    game_choice: Game_Choice
    config_data: Any
    _user_os: user_os.UserOS

    if getattr(sys, 'frozen', False):  # if running as PyInstaller onefile
        _app_dir = Path(sys.executable).resolve().parent
    else:
        _app_dir = Path(__main__.__file__).resolve().parent
    config_path = _app_dir / "config.json"

    def __init__(self):
        text = [
            "Which game are you changing sensitivity for?",
            *[f"{i + 1} - {choice.value}" for i, choice in enumerate(Game_Choice)],
        ]
        self.game_choice: Game_Choice = try_input(
            self.__input_to_game_choice, text=text, prompt="Type # and press enter: "
        )

        CurrentUserOS = (
            user_os.Windows if platform.system() == "Windows" else user_os.Linux
        )
        self._user_os = CurrentUserOS(self.game_choice)

        self.config_data = self.load_config()
        self.save_config()

    def load_config(self) -> Any:
        try:
            with open(self.config_path) as config:
                return json.load(config)
        except FileNotFoundError:
            config = {}
            for game in Game_Choice:
                config[game.value] = {}
            return config

    def save_config(self):
        with open(self.config_path, "w") as config:
            json.dump(self.config_data, config)

    def get_data(self, key: str) -> Any:
        try:
            return self.config_data[self.game_choice.value][key]
        except KeyError:
            return

    def set_data(self, key: str, value: Any):
        self.config_data[self.game_choice.value][key] = value
        self.save_config()

    @property
    def user_os(self) -> user_os.UserOS:
        return self._user_os

    @staticmethod
    def __input_to_game_choice(input: str) -> Game_Choice:
        if input == "1":
            return Game_Choice.BL2
        elif input == "2":
            return Game_Choice.TPS
        elif input == "3":
            return Game_Choice.TTA
        else:
            raise IndexError


CONFIG = Config()
