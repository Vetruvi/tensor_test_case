from selenium.webdriver.common.by import By

class ContactsPageLocators():
    TENSOR_BANNER = (By.CSS_SELECTOR, '.mb-12')
    REGION_CHOOSED = (By.XPATH, '//span[@class = "sbis_ru-Region-Chooser ml-16 ml-xm-0"]/span')
    CHOOSE_REGION = (By.XPATH, '//span[@title = "Камчатский край"]')
    CITY = (By.ID, 'city-id-2')

class MainPageLocators():
    CONTACTS = (By.XPATH, '//ul[@class = "sbisru-Header__menu ws-flexbox ws-align-items-center"]//li[2]//a')
    DOWNLOAD_SBIS = (By.XPATH, '//div[@class = "sbisru-Footer__cell pb-16 pb-sm-8"][10]/ul/li[6]//a')
    

class DownloadPageLocators():
    PLUGIN = (By.XPATH, '//div[@data-id = "plugin"]//div[@class = "controls-tabButton__overlay"]')
    DOWNLOAD_LINK = (By.XPATH, '//a[@href = "https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
    
class TensorPageLocators():
    POWER_HUMANS = (By.CSS_SELECTOR, '.tensor_ru-Index__card-title')
    ABOUT = (By.XPATH, '//div[@class = "tensor_ru-Index__block4-content tensor_ru-Index__card"]//a')
    IMAGE_ABOUT_FIRST = (By.XPATH, '//div[@class = "s-Grid-col s-Grid-col--3 tensor_ru-About--col-md6 tensor_ru-About__block3--col-sm12"][1]//img')
    IMAGE_ABOUT_SECOND = (By.XPATH, '//div[@class = "s-Grid-col s-Grid-col--3 tensor_ru-About--col-md6 tensor_ru-About__block3--col-sm12"][2]//img')
    IMAGE_ABOUT_THIRD = (By.XPATH, '//div[@class = "s-Grid-col s-Grid-col--3 tensor_ru-About--col-md6 tensor_ru-About__block3--col-sm12"][3]//img')
    IMAGE_ABOUT_FOURTH = (By.XPATH, '//div[@class = "s-Grid-col s-Grid-col--3 tensor_ru-About--col-md6 tensor_ru-About__block3--col-sm12"][4]//img')
    