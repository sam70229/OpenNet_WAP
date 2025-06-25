
from typing import Optional, TypeVar

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Locator:
    
    def __init__(self, by, value):
        self.by = by
        self.value = value


T = TypeVar("T", bound="Element")


class Element:

    def __init__(self, method: str, locator: str, page):
        self.locator = Locator(method, locator)
        self._page = page

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} object on {self._page}: {self.locator}>"
    
    @property
    def page(self):
        return self._page

    def wait(
        self,
        condition = None,
        timeout: Optional[int] = None,
        no_exception: bool = False,
    ) -> T:
        if not condition:
            condition = EC.presence_of_element_located

        if not timeout:
            timeout = 15

        try:
            WebDriverWait(self.page.driver, timeout).until(condition((self.locator.by, self.locator.value)))

        except Exception as e:
            if not no_exception:
                raise e

        return self
    
    # Properties
    @property
    def _element(self) -> WebElement:
        return self.page.driver.find_element(self.locator.by, self.locator.value)

    @property
    def text(self) -> str:
        return self._element.text
    
    @property
    def location(self) -> str:
        return self._element.location
    
    @property
    def size(self) -> str:
        return self._element.size
    
    @property
    def value(self) -> str:
        return self._element.get_attribute("value")
    
    @property
    def is_visible(self) -> bool:
        is_visible = False
        try:
            is_visible = self._element.is_displayed()
        except NoSuchElementException:
            pass
        except Exception as e:
            raise e
        return is_visible
    
    # actions
    def click(self) -> None:
        self._element.click()

    def input(self, value: str) -> None:
        self._element.send_keys(str(value))

    def clear(self) -> None:
        self._element.clear()
