from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""""Parent class"""
"""contains general methods and utilities"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 150).until(EC.visibility_of_element_located(by_locator)).click()

    def do_hover_over(self, by_locator):
        element_to_hover_over = WebDriverWait(self.driver, 150).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element_to_hover_over).perform()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 150).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 150).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 150).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_page_title(self, title):
        WebDriverWait(self.driver, 150).until(EC.title_is(title))
        return self.driver.title
