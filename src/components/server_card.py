from dataclasses import dataclass
from typing import Any, Optional

from components.page_component import PageComponent
from playwright.sync_api import Page


@dataclass
class SrvSpecification:
    cpu: Optional[str] = None
    ram: Optional[str] = None
    disk: Optional[str] = None
    os: Optional[str] = None
    connection_speed: Optional[str] = None
    traffic: Optional[str] = None


class ServerCard(PageComponent):
    def __init__(self, page: Page, locator: str):
        super().__init__(page, locator)
        self.server_id: Optional[str] = None
        self.price: Optional[float] = None
        self.currency: Optional[str] = None
        self.location: Optional[str] = None
        self.specs = SrvSpecification()

        self.initialize()

    def initialize(self) -> None:
        self.update()

    def update(self) -> None:
        pass

    def get_server_details(self) -> dict[str, Any]:
        return {
            'server_id': self.server_id,
            'price': self.price,
            'currency': self.currency,
            'specs': self.specs,
            'location': self.location
        }

    def get_price(self) -> Optional[float]:
        return self.price
