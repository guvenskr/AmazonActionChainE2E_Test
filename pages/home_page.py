from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    LOGIN_BTN = (By.ID, 'nav-link-accountList-nav-line-1')
    USER_NAME_TEXT = (By.ID, 'nav-link-accountList-nav-line-1')
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')

    def click_login_btn(self):
        self.click_element(*self.LOGIN_BTN)

        return LoginPage(self.driver)

    def get_user_name(self):
        return self.wait_element(self.USER_NAME_TEXT).text

    def click_search_box(self, search_text):
        self.click_element(*self.SEARCH_BOX).send_text(search_text + Keys.ENTER, *self.SEARCH_BOX)
