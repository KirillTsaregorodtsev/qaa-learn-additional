from typing import List

from components.page_component import PageComponent
from playwright.sync_api import Page

class Toggle(PageComponent):
    def __init__(self, page: Page, locator: str, toggle_type: str, options: List[str]):
        super().__init__(page, locator)
        self.toggle_type = toggle_type
        self.options = options
        self.selected_option = options[0]

    def select_option(self, option: str) -> None:
        pass

    def get_selected_option(self) -> str:
        return self.selected_option

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        pass