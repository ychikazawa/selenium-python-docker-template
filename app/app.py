import os
from selenium import webdriver
from logging import DEBUG, INFO
import chromedriver_binary  # Adds chromedriver binary to path

from logger_manager import get_logger
from utils import get_current_datetime_str

logger = get_logger(__name__, INFO)


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Remote(
    command_executor = os.environ['SELENIUM_URL'],
    options = options,
)

driver.get("https://www.google.com")

logger.info(driver.title)
screenshot_path = f"log/{get_current_datetime_str()}_{driver.title}.png"
driver.save_screenshot(screenshot_path)

driver.quit()
