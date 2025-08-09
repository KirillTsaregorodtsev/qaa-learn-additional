from typing import List, Optional

from components.filter import Filter
from playwright.sync_api import Page


class Toggle(Filter):
    def __init__(self, page: Page, locator: str, filter_type: str, options: List[str]):
        super().__init__(page, locator, filter_type)
        self.options = options
        self.selected_option: Optional[str] = None
        self.initialize()

    def select_option(self, option: str) -> None:
        self.selected_option = option

    def get_selected_option(self) -> Optional[str]:
        return self.selected_option

    def apply_filter(self, value: str) -> None:
        if value in self.options:
            self.select_option(value)
        else:
            raise ValueError(f"Option '{value}' is not a valid option for this toggle.")

    def reset_filter(self) -> None:
        if self.options:
            self.select_option(self.options[0])

    def get_current_value(self) -> Optional[str]:
        return self.get_selected_option()

    def initialize(self) -> None:
        self.update()

    def update(self) -> None:
        pass
