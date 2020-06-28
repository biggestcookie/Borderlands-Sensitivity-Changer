import json
import os
from typing import Any


def load_config() -> Any:
    config_path = f"{os.path.dirname(os.path.realpath(__file__))}\\config.json"
    try:
        with open(config_path) as config:
            return json.load(config)
    except Exception:
        return
