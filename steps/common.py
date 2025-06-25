from __future__ import annotations

import time
import logging
from typing import TYPE_CHECKING
from hamcrest import assert_that, contains_string

from selenium.common.exceptions import NoAlertPresentException

if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver

logger = logging.getLogger(__name__)

def page_is_ready(driver: WebDriver) -> bool:
    """Check DOM status code and wait for the page is fully loaded."""
    is_page_ready = False
    # Get current time
    start_time = time.time()
    # Check webpage status in 60 seconds
    while time.time() < start_time + 60:
        page_state = driver.execute_script("return document.readyState;")

        # Page status is interactive
        if page_state in ("interactive", "complete"):
            logger.debug("DOM is now interactive, total waiting time is %s" % (start_time))
            is_page_ready = True
            break

        # Page status is not interactive, wait and keep checking
        else:
            time.sleep(0.1)
            logger.debug("DOM is not fully loaded yet, current waiting time is %s" % (start_time))
    return is_page_ready

def go_to_url(driver: WebDriver, url: str) -> None:
    if not url.startswith("https") or not url.startswith("http"):
        assert False, "url must starts with either http or https"
    
    driver.get(url)

    assert_that(driver.current_url, contains_string(url), "browser url is not same as the target url")

def scroll(driver: WebDriver, direction: str):
    #     window_size = driver.get_window_size()
    #     container_rect = Rect(x=0, y=0, width=float(window_size["width"]), height=float(window_size["height"]))
    #     xi = xf = int(container_rect.x + container_rect.width * 0.5)
    #     yi = yf = int(container_rect.y + container_rect.height * 0.5)
    #     match direction:
    #         case "down":
    #             yi = int(container_rect.y + container_rect.height * (1 - 0.3))
    #             yf = int(container_rect.y + container_rect.height * 0.3)
    #     action = ActionChains(driver)
    #     action.move_to_element(pages.category_page.first_stream_thumbnail.wait()._element)
    #     action.move_by_offset(xoffset=xi, yoffset=yi)
    #     action.click_and_hold()
    #     action.move_by_offset(xoffset=xf, yoffset=yf)
    #     action.release()
    #     action.perform()

    if direction not in ("up", "down", "left", "right"):
        raise ValueError(f"{direction} is not supported,")

    direction_cmd = ""

    match direction:
        case "down":
            direction_cmd = "(0, window.innerHeight * 0.5)"

        case "up":
            direction_cmd = "(window.innerHeight * 0.5, 0)"


    driver.execute_script(f"window.scrollBy{direction_cmd};")
    

def take_screenshot(driver: WebDriver, filepath: str):
    driver.get_screenshot_as_file(filepath)


def handle_alert(driver: WebDriver):
    try:
        driver.switch_to.alert.accept()
    except NoAlertPresentException:
        pass
    except Exception as e:
        logger.exception(e)
        raise e
        