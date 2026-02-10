from macpy.core import BaseController, CommandResult



class AudioController(BaseController):

    @staticmethod
    def set_volume(volume: int) -> CommandResult:
        return AudioController._execute(
            [
                "osascript",
                "-e",
                f"set volume output volume {volume}"
            ],
        )
