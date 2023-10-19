from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page
from support.logger import logger


class LoginPage(Page):

    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a.login-button.w-button')
    ENTER_NEW_PASS = (By.ID, 'Enter-new-password')
    REPEAT_PASS = (By.ID, 'Repeat-password')

    def open_login_page(self):
        self.open_url('sign in')

    def page_log_in(self):
        self.input_text('salavatpct33@gmail.com', *self.EMAIL_FIELD)
        self.input_text('$Sea314059', *self.PASSWORD_FIELD)
        sleep(2)
        self.click(*self.CONTINUE_BUTTON)

    def input_text_field(self):
        self.input_text('test', *self.ENTER_NEW_PASS)
        self.input_text('test', *self.REPEAT_PASS)

