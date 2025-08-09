from abc import abstractmethod
from typing import Any

from components.page_component import PageComponent
from playwright.sync_api import Page


class Filter(PageComponent):
    def __init__(self, page: Page, locator: str, filter_type: str):
        super().__init__(page, locator)
        self.filter_type = filter_type

    @abstractmethod
    def reset_filter(self) -> None:
        pass

    @abstractmethod
    def apply_filter(self, value: Any) -> None:
        pass

    @abstractmethod
    def get_current_value(self) -> Any:
        pass

    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass
