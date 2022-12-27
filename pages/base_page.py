from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.action = ActionChains(self.driver)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.find_element(*locator).click()

        return self

    def send_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def clear_text(self, *locator):
        self.find_element(*locator).clear()

        return self

    def wait_element(self, method, message=''):
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def present_element(self, method, message=''):
        return self.wait.until(ec.presence_of_element_located(method), message)

    def find_elements(self, index, *element):
        return self.driver.find_elements(*element)[index]

    def get_url(self):
        return self.driver.current_url

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        self.action.move_to_element(element).perform()
