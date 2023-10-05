from .main_page import MainPage
from .locators import DownloadPageLocators
import wget
import os

class DownloadPage(MainPage):

    def download_plugin(self):
        MainPage.is_element_clickable_wait(self, DownloadPageLocators.PLUGIN)
        self.browser.find_element(*DownloadPageLocators.PLUGIN).click()
        MainPage.is_element_clickable_wait(self, DownloadPageLocators.DOWNLOAD_LINK)
        Link = self.browser.find_element(*DownloadPageLocators.DOWNLOAD_LINK).get_attribute("href")
        wget.download(Link)
        
    def check_downloaded_plugin(self):
        assert os.path.exists("sbisplugin-setup-web.exe"), "Файл не был скачан"

    def check_size_file(self):
        Link = self.browser.find_element(*DownloadPageLocators.DOWNLOAD_LINK)
        file_size = os.stat('sbisplugin-setup-web.exe')
        Link_size_file = float(Link.text.split(" ")[2])
        file_size_mb = round(float(file_size.st_size / 1048576), 2)
        MainPage.is_first_element_should_equal_second(self, Link_size_file, file_size_mb)