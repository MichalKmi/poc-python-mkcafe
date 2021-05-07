import time

from config.config import TestData
from pages.login_page import LoginPage
from tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login_to_a_page(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.USER_PASSWORD)
        flag = self.loginPage.is_sign_out_visible()
        assert flag

    def test_dashboard(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_logged_dashboard_exist()
        assert flag

    def test_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_logout()
        time.sleep(0.5)
        self.loginPage.expand_menu()
        flag = self.loginPage.is_sign_in_visible()
        assert flag

    def tear_down(self):
        self.selenium.stop()


