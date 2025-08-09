from abc import ABC, abstractmethod

from playwright.sync_api import Page


class PageComponent(ABC):
    def __init__(self, page: Page, locator: str):
        self.page = page
        self.element = page.locator(locator)

    @abstractmethod
    def update(self):
        pass
