from __future__ import annotations

import logging
import yaml
from pathlib import Path
from logging.config import dictConfig
from typing import TYPE_CHECKING

from fixtures import *

if TYPE_CHECKING:
    from _pytest.reports import TestReport
    from selenium.webdriver.remote.webdriver import WebDriver


LOGGING_CONFIG_PATH = "config/logging.yaml"
logging_config_dict = yaml.safe_load(open(LOGGING_CONFIG_PATH))

# Create log file folder if needed
log_file_path = Path(logging_config_dict["handlers"]["File"]["filename"])
log_file_path.parent.mkdir(parents=True, exist_ok=True)

dictConfig(logging_config_dict)
logger = logging.getLogger(__name__)
logger.info(f"Logging config loaded from: {LOGGING_CONFIG_PATH}")


def pytest_runtest_teardown(item, nextitem):
    driver: WebDriver = item.funcargs["driver"]
    driver.get_screenshot_as_file("logs/error_screenshot.png")
