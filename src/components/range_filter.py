from typing import Tuple

from components.filter import Filter
from playwright.sync_api import Page


class RangeFilter(Filter):
    def __init__(self, page: Page, locator: str, filter_type: str, min_value: int, max_value: int):
        super().__init__(page, locator, filter_type)
        self.min_boundary = min_value
        self.max_boundary = max_value
        self.current_min = min_value
        self.current_max = max_value

    def set_range(self, min_val: int, max_val: int) -> None:
        self.current_min = min_val
        self.current_max = max_val

    def get_range(self) -> Tuple[int, int]:
        return self.current_min, self.current_max

    def apply_filter(self, value: Tuple[int, int]) -> None:
        min_val, max_val = value
        self.set_range(min_val, max_val)

    def reset_filter(self) -> None:
        self.set_range(self.min_boundary, self.max_boundary)

    def get_current_value(self) -> Tuple[int, int]:
        return self.get_range()

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        pass
