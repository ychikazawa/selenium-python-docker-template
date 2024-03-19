import os
from logging import DEBUG, INFO

from logger_manager import get_logger
from utils import get_current_datetime_str
from driver_context import DriverContext

logger = get_logger(__name__, INFO)


with DriverContext('remote') as driver:

    driver.get("https://www.google.com")

    logger.info(driver.title)
    screenshot_path = f"log/{get_current_datetime_str()}_{driver.title}.png"
    driver.save_screenshot(screenshot_path)

