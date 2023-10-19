from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_INPUT = (By.ID, 'ap_email')

    def signin_page_opened(self):
        # context.driver.get('https://www.amazon.com/')
        # expected_text = 'Sign in'
        # actual_text = self.driver.find_element(*self.SIGNIN_HEADER).text
        # assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
        self.verify_text('Sign in', *self.SIGNIN_HEADER)
        self.driver.find_element(*self.EMAIL_INPUT)
        self.verify_partial_url('ap/signin')

