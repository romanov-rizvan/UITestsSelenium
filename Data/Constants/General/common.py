import pytest
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseTest(object):

    @pytest.fixture(scope="class", autouse=True)
    def manage_driver(self, d):
        d.start()
        yield d
        d.stop()

    @staticmethod
    def wait_present(driver, xpath, timeout=15.0):
        try:
            WebDriverWait(driver, timeout).until(ec.presence_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def wait_not_present(driver, xpath, timeout=2.0):
        try:
            WebDriverWait(driver, timeout).until_not(ec.presence_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def click_on(driver, xpath, delay=0.5):
        try:
            driver.find_element("xpath", xpath).click()
        except:
            time.sleep(delay)
            driver.find_element("xpath", xpath).click()

    @staticmethod
    def refresh_page(driver):
        driver.instance.refresh()

    @staticmethod
    def current_url(driver):
        return driver.instance.current_url

    @staticmethod
    def get_web_element(driver, xpath):
        return driver.instance.find_element("xpath", xpath)

    @staticmethod
    def get_web_elements(driver, xpath):
        return driver.instance.find_elements("xpath", xpath)
