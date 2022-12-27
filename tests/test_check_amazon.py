from pages.base_page import BasePage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.list_page import ListPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestCheckAmazon(BaseTest):
    valid_email = 'guvensekertest@gmail.com'
    password = 'Qwer123.'
    user_name = 'guven'
    search_text = 'samsung'
    page_number = '2'

    def test_check_amazon(self):
        home_page = HomePage(self.driver)
        base_page = BasePage(self.driver)
        self.assertIn(BaseTest.base_url, base_page.get_url(), "İstenilen sayfada değilsin")
        login_page = home_page.click_login_btn()

        login_page.fill_email_text_box(self.valid_email)
        login_page.click_continue_btn()
        login_page.fill_password_text_box(self.password)
        login_page.click_giris_yap_btn()
        self.assertEqual(self.user_name, home_page.get_user_name(), "Giris basarisiz")

        home_page.click_search_box(self.search_text)
        category_page = CategoryPage(self.driver)
        self.assertIn(self.search_text, category_page.get_searched_text())
        category_page.click_selected_page()
        self.assertEqual(category_page.active_page().text, '2', "2. sayfada degilsin!")

        category_page.click_third_row_product(9)
        product_page = ProductPage(self.driver)
        selected_product = product_page.get_product_name()
        product_page.click_add_to_list()
        product_page.click_close_add_to_list_popup()
        product_page.hover_account_click_list()

        list_page = ListPage(self.driver)
        self.assertEqual(selected_product, list_page.get_listed_product_name(), 'Ürünler eşleşmedi')
        list_page.click_remove_product()
        self.assertTrue(list_page.is_remove_success(), 'Ürün silinemedi')
