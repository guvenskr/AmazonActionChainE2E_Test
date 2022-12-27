from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ListPage(BasePage):
    ITEM_REMOVE_BTN = (By.NAME, 'submit.deleteItem')
    LISTED_PRODUCT_TXT = (By.TAG_NAME, 'h2')
    REMOVE_SUCCESS = (By.XPATH, '//div[text()="Silindi"]')

    def click_remove_product(self):
        self.click_element(*self.ITEM_REMOVE_BTN)

    def get_listed_product_name(self):
        return self.wait_element(self.LISTED_PRODUCT_TXT).text

    def is_remove_success(self):
        return self.present_element(self.REMOVE_SUCCESS)
