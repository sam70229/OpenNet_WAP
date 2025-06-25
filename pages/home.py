from selenium.webdriver.common.by import By

from lib.element import Element

from .page import Page

class HomePage(Page):

    @property
    def browse_tab(self) -> Element:
        return Element(By.XPATH, "//*[text()='Browse']/parent::div", self)

    

