from components.filter import Filter
from playwright.sync_api import Page

class RangeFilter(Filter):
    def __init__(self, page: Page, locator: str, filter_type: str, min_value: int, max_value: int):
        super().__init__(page, locator, filter_type)
        self.min_value = min_value
        self.max_value = max_value
        self.current_min = None
        self.current_max = None

    def set_range(self, min: int, max: int) -> None:
        pass

    def get_range(self) -> tuple[int, int]:
        pass

    def apply_filter(self, value: dict[str, int]) -> None:
        pass

    def reset_filter(self) -> None:
        pass

    def get_current_value(self) -> dict[str, int]:
        pass