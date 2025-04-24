from selenium import webdriver # type: ignore


class SeleniumDriver:
    def __init__(self):
        self._driver = webdriver.Chrome()

    def get_driver(self):
        return self._driver

    def close_driver(self):
        if self._driver:
            self._driver.close()
