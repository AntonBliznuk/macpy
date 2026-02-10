from dataclasses import dataclass


@dataclass
class CommandResult:
    success: bool
    message: str
    error: str | None = None
