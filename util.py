from typing import Any, Callable


def try_input(
    func: Callable, prompt: str = "", error: str = "Not a valid choice"
) -> Any:
    while True:
        try:
            return func(input(prompt))
        except Exception:
            print(error)
