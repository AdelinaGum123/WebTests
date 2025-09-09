import allure

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
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_LINK = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    RECOVERY_BUTTON =(By.XPATH, ' //*[@name="st.go_to_recovery"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка корректности загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_RESTORE)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.REGISTER_BUTTON)
        self.find_element(LoginPageLocators.SOCIAL_ICON_MAILRU)
        self.find_element(LoginPageLocators.SOCIAL_ICON_VK)
        self.find_element(LoginPageLocators.SOCIAL_ICON_YANDEX)


    @allure.step('Клик по кнопке "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Нахождение текста ошибки на экране')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Ввод данных в инпут логина')
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Ввод данных в инпут пароля')
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVERY_BUTTON).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()