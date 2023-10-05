from .main_page import MainPage
from .locators import TensorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorPage(MainPage):

    def should_be_power_humans(self):
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located(TensorPageLocators.POWER_HUMANS))
        power_humans = self.browser.find_element(*TensorPageLocators.POWER_HUMANS)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", power_humans)
        MainPage.is_element_present(self, *TensorPageLocators.POWER_HUMANS)

    def go_about_page_from_tensor_page(self):
        self.browser.find_element(*TensorPageLocators.ABOUT).click()
        MainPage.is_first_element_should_equal_second(self, self.browser.current_url, "https://tensor.ru/about")

    def check_height_width_images_on_tensor_page(self):
        first_image_width = self.browser.find_element(*TensorPageLocators.IMAGE_ABOUT_FIRST).get_attribute("width")
        first_image_height = self.browser.find_element(*TensorPageLocators.IMAGE_ABOUT_FIRST).get_attribute("height")
        second_image_width = self.browser.find_element(*TensorPageLocators.IMAGE_ABOUT_SECOND).get_attribute("width")
        second_image_height = self.browser.find_element(*TensorPageLocators.IMAGE_ABOUT_SECOND).get_attribute("height")
        third_image_width = self.browser.find_element(*TensorPageLocators.IMAGE_ABOUT_THIRD).get_attribute("width")
        third_image_height = self.browser.find_element(*TensorPageLocators.IMAGE_ABOUT_THIRD).get_attribute("height")
        fourth_image_width = self.browser.find_element(*TensorPageLocators.IMAGE_ABOUT_FOURTH).get_attribute("width")
        fourth_image_height = self.browser.find_element(*TensorPageLocators.IMAGE_ABOUT_FOURTH).get_attribute("height")
    
        assert first_image_width == second_image_width == third_image_width == fourth_image_width, \
            "The width is not the same for all images"
        
        assert first_image_height == second_image_height == third_image_height == fourth_image_height, \
            "The height is not the same for all images"
