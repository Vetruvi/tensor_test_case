from .main_page import MainPage
from .locators import ContactsPageLocators

class ContactPage(MainPage):

    def banner_tensor_click(self):
        self.browser.find_element(*ContactsPageLocators.TENSOR_BANNER).click()

    def check_region_choosed(self):
        region = self.browser.find_element(*ContactsPageLocators.REGION_CHOOSED).text
        MainPage.is_first_element_should_equal_second(self, region, "Республика Башкортостан")

    def change_region(self):
        MainPage.is_element_clickable_wait(self, ContactsPageLocators.REGION_CHOOSED)
        self.browser.find_element(*ContactsPageLocators.REGION_CHOOSED).click()

        MainPage.is_element_clickable_wait(self, ContactsPageLocators.CHOOSE_REGION)
        self.browser.find_element(*ContactsPageLocators.CHOOSE_REGION).click()

    def check_region_changed_to_Kamchatka(self):
        MainPage.wait_where_first_element_equal_second(self, ContactsPageLocators.REGION_CHOOSED, "Комчатский край")

        City = self.browser.find_element(*ContactsPageLocators.CITY).text
        MainPage.is_first_element_should_equal_second(self, City, "Петропавловск-Камчатский")