from selenium.webdriver.common.by import By

from lib.element import Element

from .page import Page


class BrowsePage(Page):

    @property
    def search_input(self) -> Element:
        return Element(By.XPATH, "//input[@type='search']", self)    
    
    def search_result(self, text: str) -> Element:
        return Element(By.XPATH, f"//*[@title='{text}']", self)
    
    def search_category_result(self, text: str) -> Element:
        return Element(By.XPATH, f"//img[@alt='{text}']/ancestor::div[3]//p[@title='{text}']", self)