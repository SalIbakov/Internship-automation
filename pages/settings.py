from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from support.logger import logger


class SettingsMenu(Page):

    CHANGE_PASS_BTN = (By.CSS_SELECTOR, 'a[href="/set-new-password"].page-setting-block.w-inline-block')

    def password_change(self):
        self.click(*self.CHANGE_PASS_BTN)
