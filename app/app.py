import argparse
from logging import DEBUG, INFO

from logger_manager import get_logger
from utils import get_current_datetime_str
from driver_context import DriverContext

logger = get_logger(__name__, INFO)


def parse_args():
    parser = argparse.ArgumentParser(description='Auto reservator command line arguments.')
    parser.add_argument('--sample', "-s", type=str, default='sample', help='Sample argument.')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # Parse arguments.
    parse_args = parse_args()
    sample = parse_args.sample

        
    with DriverContext() as driver:

        driver.get("https://www.google.com")

        logger.info(driver.title)
        screenshot_path = f"log/{get_current_datetime_str()}_{driver.title}.png"
        driver.save_screenshot(screenshot_path)

