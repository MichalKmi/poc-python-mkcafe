from selenium.webdriver.common.by import By
from config.config import TestData
from pages.base_page import BasePage
import json
import time

with open('data/data_wrong.json') as f:
# with open('data/data.json') as f:
    uiRepo = json.load(f)


class Navigation(BasePage):
    LEFT_EXPANDED_LIST_SELECTOR = (By.CSS_SELECTOR, ".show-me > div > div.category-list-wrap")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def main_links_texts_matches_expected(self, element_number):
        MENU_ELEMENT = By.CSS_SELECTOR, f'.h-full > ul li:nth-child({element_number})'
        MENU_ELEMENT_INNER_TEXT = self.get_element_text(MENU_ELEMENT)
        TXT_FROM_JSON = uiRepo[f"menu {element_number}"]
        self.is_visible(MENU_ELEMENT)
        self.do_click(MENU_ELEMENT)
        isResultsProperBoolean = MENU_ELEMENT_INNER_TEXT == TXT_FROM_JSON
        time.sleep(1)
        return isResultsProperBoolean

    def hover_over_three_first_options(self, element_number):
        MENU_ELEMENT = By.CSS_SELECTOR, f'.h-full > ul li:nth-child({element_number})'
        self.is_visible(MENU_ELEMENT)
        time.sleep(1)
        self.do_hover_over(MENU_ELEMENT)
        time.sleep(1)
        self.is_visible(self.LEFT_EXPANDED_LIST_SELECTOR)
        EXPANDED_LIST_INNER_TEXT = self.get_element_text(self.LEFT_EXPANDED_LIST_SELECTOR)
        TXT_FROM_JSON = uiRepo[f"menu {element_number} expandedLeftListInner"]
        isResultsProperBoolean = EXPANDED_LIST_INNER_TEXT == TXT_FROM_JSON
        return isResultsProperBoolean
