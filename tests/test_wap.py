import logging
import time

from dataclasses import dataclass
from hamcrest import assert_that, equal_to
from selenium.webdriver.remote.webdriver import WebDriver

from pages import Pages
from steps.common import (
    page_is_ready,
    go_to_url,
    scroll,
    take_screenshot,
    handle_alert,
)
from steps.search import search_stream

logger = logging.getLogger(__name__)

@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float
    

def test_wap(driver: WebDriver, pages: Pages):
    # Go to Twitch.tv
    go_to_url(driver, "https://m.twitch.tv")

    # Click in the search icon
    search_stream(pages, "StarCraft II")

    # Scroll down 2 times
    for _ in range(2):
        scroll(driver, "down")
        time.sleep(1)

    # Select one streamer
    pages.category_page.stream_streamer_text(3).wait().click()

    # on the streamer page wait until all is load and take a screenshot
    # did not see any modals, so no clue on how to handle it,
    # handle window alert for now
    handle_alert(driver)

    assert_that(page_is_ready(driver), equal_to(True))

    assert_that(
        pages.streamer_page.steamer_name.wait(no_exception=True).is_visible,
        equal_to(True),
        "Streamer Name is not showing"
    )
    
    assert_that(
        pages.streamer_page.streamer_video.wait(no_exception=True).is_visible,
        equal_to(True),
        "Streamer Page does not have any video"
    )

    take_screenshot(driver, "logs/screenshot.png")
