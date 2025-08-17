from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_RESTORE = (By.XPATH, '//*[@data-l="t,restore"]')
    PASSWORD_FIELD = (By.ID, 'field_password')
    REGISTER_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    SOCIAL_ICON_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    SOCIAL_ICON_MAILRU = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    SOCIAL_ICON_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')


class LoginPageWelper(BasePage):
    pass