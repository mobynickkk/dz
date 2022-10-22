from dataclasses import dataclass


@dataclass
class State:
    identifier: str
    final: bool
