import pytest

from selenium import webdriver

from selenium.webdriver.remote.webdriver import WebDriver

@pytest.fixture(scope="class")
def driver():
    web_driver: WebDriver = None

    mobile_emulation = { "deviceName": "iPhone 12 Pro" }
    # mobile_emulation = { "deviceName": "Pixel 7" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--incognito")

    # caps = chrome_options.to_capabilities()

    web_driver = webdriver.Chrome(options=chrome_options)

    yield web_driver

    web_driver.quit()


@pytest.fixture(scope="class")
def pages(driver: WebDriver):
    from pages import Pages
    pages = Pages(driver)
    yield pages
