from selenium.webdriver.common.by import By

from lib.element import Element

from .page import Page


class CategoryPage(Page):

    def stream_thumbnail(self, index: int) -> Element:
        return Element(By.XPATH, f"(//button[contains(@class, 'ScCoreLink')])[{index}]", self)
    
    def stream_streamer_text(self, index: int) -> Element:
        return Element(By.XPATH, f"(//a[contains(@class, 'ScCoreLink') and contains(@href, 'home')])[{index}]", self)

    def stream_title(self, value: str) -> Element:
        return Element(By.XPATH, f"//a[contains(@class, 'ScCoreLink') and text()='{value}']", self)
    
    def streamer_account(self, value: str) -> Element:
        return Element(By.XPATH, f"//a[contains(@class, 'ScCoreLink') and text()='{value} and contains(@href, 'home')]", self)