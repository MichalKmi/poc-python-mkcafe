from selenium.webdriver.common.by import By
from config.config import TestData
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    LOGIN_EXPANDABLE_LINK = (By.XPATH, "//div[contains(text(), 'Moje konto')]")
    EMAIL = (By.XPATH, '//div[1]/div/div/input')
    PASS = (By.XPATH, '//div[2]/div/div/input')
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Zaloguj się')]")
    SIGN_OUT_LINK = (By.XPATH, "//li[contains(text(), 'Wyloguj')]")
    LOGIN_DASHBOARD_LINK = (By.XPATH, "//div[2]/div/h1[contains(text(), 'Mój panel')]")
    ACCOUNT_PANEL_LINK = (By.XPATH, "//li[contains(text(), 'Panel Konta')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def expand_menu(self):
        self.do_click(self.LOGIN_EXPANDABLE_LINK)
        time.sleep(1)

    def get_login_page_title(self, title):
        return self.get_page_title(title)

    def is_sign_out_visible(self):
        self.expand_menu()
        return self.is_visible(self.SIGN_OUT_LINK)

    def is_sign_in_visible(self):
        self.expand_menu()
        return self.is_visible(self.SIGN_IN_BUTTON)

    def is_logged_dashboard_exist(self):
        self.do_click(self.LOGIN_EXPANDABLE_LINK)
        time.sleep(1)
        self.do_click(self.ACCOUNT_PANEL_LINK)
        return self.is_visible(self.LOGIN_DASHBOARD_LINK)

    def do_login(self, username, password):
        self.expand_menu()
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASS, password)
        self.do_click(self.SIGN_IN_BUTTON)

    def do_logout(self):
        self.expand_menu()
        self.do_click(self.SIGN_OUT_LINK)


