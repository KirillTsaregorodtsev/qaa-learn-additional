from typing import Any

from components.page_component import PageComponent
from playwright.sync_api import Page


class SrvSpecification:
    pass


class ServerCard(PageComponent):
    def __init__(
        self,
        page: Page,
        locator: str,
        server_id: str,
        server_name: str,
        price: float,
        currency: str,
        specs: SrvSpecification,
        location: str
    ):
        super().__init__(page, locator)
        self.server_id: str = server_id
        self.server_name: str = server_name
        self.price: float = price
        self.currency: str = currency
        self.specs: SrvSpecification = specs
        self.location: str = location

    def get_server_details(self) -> dict[str, Any]:
        return {
            'server_id': self.server_id,
            'server_name': self.server_name,
            'price': self.price,
            'currency': self.currency,
            'specs': self.specs,
            'location': self.location
        }

    def get_price(self) -> float:
        pass

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        pass