from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    CLICK_FIRST_ITEM = (By.CSS_SELECTOR, ' .a-price-whole')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#productTitle')

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def click_on_first_product(self):
        self.click(*self.CLICK_FIRST_ITEM)

    def store_product_name(self):
        return self.find_element(*self.PRODUCT_NAME).text

