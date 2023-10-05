from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def is_first_element_should_in_second(self, first_element, second_element):
        assert first_element in second_element, f"{first_element} not in {second_element}"

    def is_first_element_should_equal_second(self, first_element, second_element):
        assert first_element == second_element, f"{first_element} not equal {second_element}"

    def wait_where_first_element_equal_second(self, list_how_what, second_element, timeout=4):
        try: WebDriverWait(self.browser, timeout).until(
            EC.text_to_be_present_in_element(list_how_what, second_element)
            )
        except TimeoutException:
            f"{self.browser.find_element(*list_how_what).text} not equal {second_element}"
            return False
        return True
        
    def is_element_clickable_wait(self, list_how_what):
        try:
            WebDriverWait(self.browser, 4).until(EC.element_to_be_clickable(list_how_what))
        except TimeoutException:
            f"{self.browser.find_element(*list_how_what).text} not clickable"
            return False
        return True

    def open_second_tab(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def enter_click(self, how, what):
        self.browser.find_element(how, what).send_keys(Keys.ENTER)

    def open(self):
        self.browser.get(self.url)