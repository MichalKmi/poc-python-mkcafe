from pages.navigation import Navigation
from tests.test_base import BaseTest


class TestNavigation(BaseTest):

    def test_main_links_texts_matches_expected(self):
        self.navigation = Navigation(self.driver)
        for i in range(6):
            number = str(i + 1)
            flag = self.navigation.main_links_texts_matches_expected(number)
            assert flag, f'/Sth went wrong for element no {number}'

    def test_hover_over_three_first_options(self):
        self.navigation = Navigation(self.driver)
        for i in range(3):
            number = str(i + 1)
            flag = self.navigation.hover_over_three_first_options(number)
            assert flag, f'/Sth went wrong for element no {number}'

    def tear_down(self):
        self.selenium.stop()
