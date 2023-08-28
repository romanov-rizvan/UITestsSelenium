import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Data.Constants.General.config import Config


class DriverManager(object):

    def __init__(self):
        self._instance = None

    def start(self):
        # implement logic to create instance depends on condition
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self._instance = webdriver.Chrome(options=chrome_options)
        self._instance.maximize_window()
        self._instance.get(Config.url_host())
        return self._instance

    @property
    def instance(self):
        if not self._instance:
            self.start()
        return self._instance

    def stop(self):
        self._instance.quit()


@pytest.fixture(scope="module")
def d():
    return DriverManager()
