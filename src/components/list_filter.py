from components.filter import Filter
from playwright.sync_api import Page

class ListFilter(Filter):
    def __init__(self, page: Page, locator: str, filter_type: str, options: list[str]):
        super().__init__(page, locator, filter_type)
        self.options = options
        self.selected_options = []

    def select_option(self, option: str) -> None:
        pass

    def deselect_option(self, option: str) -> None:
        pass

    def get_selected_options(self) -> list[str]:
        return self.selected_options

    def get_options(self) -> list[str]:
        return self.options

    def apply_filter(self, value: list[str]) -> None:
        pass

    def reset_filter(self) -> None:
        pass