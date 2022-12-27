from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_TEXT_BOX = (By.ID, 'ap_email')
    DEVAM_ET_BTN = (By.ID, 'continue')
    PASSWORD_TEXT_BOX = (By.ID, 'ap_password')
    GIRIS_YAP_BTN = (By.ID, 'signInSubmit')

    def fill_email_text_box(self, email):
        self.clear_text(*self.EMAIL_TEXT_BOX).send_text(email, *self.EMAIL_TEXT_BOX)

    def click_continue_btn(self):
        self.click_element(*self.DEVAM_ET_BTN)

    def click_giris_yap_btn(self):
        self.click_element(*self.GIRIS_YAP_BTN)

    def fill_password_text_box(self, password):
        self.send_text(password, *self.PASSWORD_TEXT_BOX)
