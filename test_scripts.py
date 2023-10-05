from .pages.contacts_page import ContactPage
from .pages.download_page import DownloadPage
from .pages.tensor_page import TensorPage
import pytest


@pytest.mark.first_script
def test_first_srtipt(browser):
    link = "https://sbis.ru/"
    page = ContactPage(browser, link)
    page.open()
    page.go_contacts_page()
    page.banner_tensor_click()
    page.open_second_tab()
    page = TensorPage(browser, link)
    page.should_be_power_humans()
    page.go_about_page_from_tensor_page()
    page.check_height_width_images_on_tensor_page()

@pytest.mark.second_script
def test_second_script(browser):
    link = "https://sbis.ru/"
    page = ContactPage(browser, link)
    page.open()
    page.go_contacts_page()
    page.check_region_choosed()
    page.change_region()
    page.check_region_changed_to_Kamchatka()

@pytest.mark.third_script
def test_third_script(browser):
    link = "https://sbis.ru/"
    page = DownloadPage(browser, link)
    page.open()
    page.go_download_sbis()
    page.download_plugin()
    page.check_downloaded_plugin()
    page.check_size_file()