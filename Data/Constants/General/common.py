import pytest
import random
import string
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

    @staticmethod
    def get_random_email(char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num)) + "@email.com"

    @staticmethod
    def get_random_phone_number():
        phone_num = [random.randint(2, 9)]
        phone = ""
        for i in range(1, 10):
            phone_num.append(random.randint(0, 9))
        for i in phone_num:
            phone = phone + str(i)
        return phone

    @staticmethod
    def get_phone_number_with_code_format(phone):
        return "+1(" + phone[:3] + ")" + phone[3:6] + "-" + phone[6:]