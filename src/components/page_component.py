from playwright.sync_api import Page


class PageComponent:
    def __init__(self, page: Page, locator: str):
        self.page = page
        self.element = page.locator(locator)