from typing import List, Callable

class Rule:
    def __init__(self, predicate: Callable, name: str = "rule"):
        self.predicate = predicate
        self.name = name
    def __call__(self, x) -> bool:
        return bool(self.predicate(x))
