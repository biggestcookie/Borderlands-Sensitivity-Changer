from enum import Enum
import json
import os
from typing import Any

import __main__
from util import try_input


class Game_Choice(Enum):
    BL2 = "Borderlands 2"
    TPS = "Borderlands The Pre-Sequel"


class Config:
    game_choice: Game_Choice
    config_data: Any
    config_path = f"{os.path.dirname(os.path.abspath(__main__.__file__))}\\config.json"

    def __init__(self):
        text = [
            "Which game are you changing sensitivity for?",
            *[f"{i + 1} - {choice.value}" for i, choice in enumerate(Game_Choice)],
        ]
        self.game_choice = try_input(
            self.__input_to_game_choice, text=text, prompt="Type # and press enter: "
        )
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

    @staticmethod
    def __input_to_game_choice(input: str) -> Game_Choice:
        if input == "1":
            return Game_Choice.BL2
        elif input == "2":
            return Game_Choice.TPS
        else:
            raise IndexError


CONFIG = Config()
