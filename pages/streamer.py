from lib.element import Element

from .page import Page

from selenium.webdriver.common.by import By


class StreamerPage(Page):

    @property
    def steamer_name(self) -> Element:
        return Element(
            By.XPATH,
            "//div[contains(@class, 'ScAvatar')]/parent::button/parent::div/following-sibling::div//h3[contains(@class, 'CoreText')]",
            self
        )
    
    @property
    def streamer_video(self) -> Element:
        return Element(By.TAG_NAME, "article", self)
