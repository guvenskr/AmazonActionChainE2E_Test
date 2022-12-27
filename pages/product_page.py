from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.ID, 'title')
    ADD_TO_LIST = (By.ID, 'add-to-wishlist-button-submit')
    POPUP_CLOSE = (By.CLASS_NAME, 'a-button-close')
    HOVER_AND_CLICK_LIST = (By.CLASS_NAME, 'nav-line-1-container')
    HIDDEN_LIST_BUTTON = (By.XPATH, '//*[@id="nav-flyout-wl-items"]/div/a/span')

    def get_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text

    def click_add_to_list(self):
        self.wait_element(self.ADD_TO_LIST).click()

    def click_close_add_to_list_popup(self):
        self.wait_element(self.POPUP_CLOSE).click()

    def hover_account_click_list(self):
        self.hover_element(*self.HOVER_AND_CLICK_LIST)
        self.wait_element(self.HIDDEN_LIST_BUTTON).click()
