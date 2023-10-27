from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from support.logger import logger


class SettingsMenu(Page):

    CHANGE_PASS_BTN = (By.CSS_SELECTOR, 'a[href="/set-new-password"].page-setting-block.w-inline-block')
    # CHANGE_PASS_BTN_MOBILE = (By.XPATH, "//a[contains(@href, '/set-new-password')]")
    # CHANGE_PASS_BTN_MOBILE = (By.CSS_SELECTOR, 'body > div.settings-profile-block > div.settings-block-menu > a:nth-child(11)')
    CHANGE_PASS_BTN_MOBILE = (By.CSS_SELECTOR, 'a[href="/profile-edit"].page-setting-block.w-inline-block')

    def password_change(self):
        # sleep(3)
        self.wait_for_element_clickable_click(self.CHANGE_PASS_BTN)

    def password_change_mobile(self):
        sleep(3)
        #self.wait_for_element_clickable_click(self.CHANGE_PASS_BTN_MOBILE)
        self.find_element(*self.CHANGE_PASS_BTN_MOBILE).click()


