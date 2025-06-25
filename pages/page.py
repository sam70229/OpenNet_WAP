from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver

class Page:
    def __init__(self, driver: WebDriver, pages: "Pages"):
        self.driver: WebDriver = driver
        self.pages = pages