class DisplayController:

    @staticmethod
    def get_current_resolution() -> tuple[int, int]:
        pass

    @staticmethod
    def get_current_refresh_rate() -> int:
        pass

    @staticmethod
    def get_current_brightness() -> int:
        pass

    def __init__(self, display_id: str) -> None:
        self.display_id = display_id
        self.current_resolution = None
        self.current_refresh_rate = None
        self.current_brightness = None

    def change_resolution(self, width: int, height: int) -> None:
        pass

    def change_refresh_rate(self, refresh_rate: int) -> None:
        pass

    def change_brightness(self, brightness: int) -> None:
        pass

