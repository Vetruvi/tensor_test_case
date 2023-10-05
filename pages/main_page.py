from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    
    def go_contacts_page(self):
        self.browser.find_element(*MainPageLocators.CONTACTS).click()

    def go_download_sbis(self):
        donwnload_li = self.browser.find_element(*MainPageLocators.DOWNLOAD_SBIS)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", donwnload_li)
        donwnload_li.click()
