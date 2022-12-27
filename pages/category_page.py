from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    SEARCHED_TXT = (By.CLASS_NAME, 's-breadcrumb')
    PAGE_NAVIGATION_SELECT = (By.XPATH, '//*[@aria-label="2 sayfasına git"]')
    PAGE_NAVIGATION_ACTIVE = (By.XPATH, '//*[@aria-label="Geçerli sayfa, sayfa 2"]')
    THIRD_ROW_PRODUCT = (By.CSS_SELECTOR, 'div .a-size-base-plus.a-color-base.a-text-normal')
    LISTED_PRODUCT = (By.XPATH, '//h1/span')

    def get_searched_text(self):
        return self.find_element(*self.SEARCHED_TXT).text

    def click_selected_page(self):
        self.find_element(*self.PAGE_NAVIGATION_SELECT).click()

    def active_page(self):
        return self.find_element(*self.PAGE_NAVIGATION_ACTIVE)

    def get_page_number(self):
        return self.find_element(*self.PAGE_NAVIGATION_ACTIVE)

    def click_third_row_product(self, index):
        self.find_elements(index, *self.THIRD_ROW_PRODUCT).click()

    def get_product_name(self):
        return self.find_element(*self.LISTED_PRODUCT).text
