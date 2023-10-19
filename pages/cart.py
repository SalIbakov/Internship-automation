from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class Cart(Page):
    CART_EMPTY_SIGN = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")
    CLICK_ADD_TO_CART = (By.ID, 'add-to-cart-button')
    #PRODUCT_NAME = (By.CSS_SELECTOR, '#productTitle')
    PRODUCT_NAME1 = (By.CSS_SELECTOR, '#productTitle')

    def verify_amazon_cart_page_is_empty(self):
        self.verify_text('Your Amazon Cart is empty', *self.CART_EMPTY_SIGN)
        self.driver.find_element(*self.CART_EMPTY_SIGN)
        self.verify_partial_url('gp/cart')

    #actual_result = context.driver.find_element(*CART_EMPTY_SIGN).text
    #assert actual_result == 'Your Amazon Cart is empty', f'Expected Your Amazon Cart is empty instead got {actual_result}'

    def click_add_to_cart(self):
        self.click(*self.CLICK_ADD_TO_CART)

    def open_cart_page(self):
        self.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
        sleep(2)
        self.driver.refresh()
        #context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

    def verify_correct_product(self, product_name):
        actual_name = self.find_element(*self.PRODUCT_NAME1).text
        assert product_name == actual_name, f'Expected {product_name} but got {actual_name}'

    #def verify_correct_product(self):
    # self.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')