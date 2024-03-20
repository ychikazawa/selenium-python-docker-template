import os
import time
from selenium import webdriver

class DriverContext:
    def __init__(self):
        # Create webdriver
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--headless')
        
        # impersonate webdriver
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        
        self.driver = webdriver.Remote(
            command_executor = os.environ['SELENIUM_URL'],
            options = options,
        )
        
        # impersonate webdriver
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(3)
        self.driver.quit()
