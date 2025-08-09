from components.filter import Filter
from playwright.sync_api import Page


class ListFilter(Filter):
    def __init__(self, page: Page, locator: str, filter_type: str, options: list[str]):
        super().__init__(page, locator, filter_type)
        self.options = options
        self.selected_options = []

    def select_option(self, option: str) -> None:
        self.element.locator(f"text={option}").click()
        if option not in self.selected_options:
            self.selected_options.append(option)

    def deselect_option(self, option: str) -> None:
        self.element.locator(f"text={option}").click()
        if option in self.selected_options:
            self.selected_options.remove(option)

    def get_selected_options(self) -> list[str]:
        return self.selected_options

    def get_options(self) -> list[str]:
        return self.options

    def apply_filter(self, value: list[str]) -> None:
        self.reset_filter()
        for option in value:
            self.select_option(option)

    def reset_filter(self) -> None:
        for option in list(self.selected_options):
            self.deselect_option(option)

    def get_current_value(self) -> list[str]:
        return self.get_selected_options()

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        pass