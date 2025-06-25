from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver

from .home import HomePage
from .browse import BrowsePage
from .category import CategoryPage
from .streamer import StreamerPage


class Pages:
    def __init__(self, driver: WebDriver):
        self.twich_home_page = HomePage(driver, self)
        self.browse_page = BrowsePage(driver, self)
        self.category_page = CategoryPage(driver, self)
        self.streamer_page = StreamerPage(driver, self)



__all__ = ['Pages']
