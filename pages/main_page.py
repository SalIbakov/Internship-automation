from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page
from support.logger import logger


class MainPage(Page):

    CLICK_SETTING_BTN = (By.CSS_SELECTOR, 'a[href="/settings"].menu-button-block.w-inline-block')
    # CLICK_SETTING_BTN = (By.CSS_SELECTOR, 'a[href="/settings"] div.menu-button-text')
    CHANGE_NEW_PASS_BTN = (By.CSS_SELECTOR, 'a.submit-button-2.w-button')
    CLICK_SETTINGS_BTN_MOBILE = (By.CSS_SELECTOR, 'a[href="/settings"].menu-button-wrapper.w-inline-block')

    def click_settings(self):
        sleep(3)
        self.wait_for_element_clickable_click(self.CLICK_SETTING_BTN)

    def click_settings_mobile(self):
        self.click(*self.CLICK_SETTINGS_BTN_MOBILE)
        sleep(3)

    def open_main(self):
        self.open_url()

    def correct_page_open(self):
        self.verify_partial_url('https://soft.reelly.io/set-new-password')

    def verify_btn_available(self):
        self.wait_for_element_appear(*self.CHANGE_NEW_PASS_BTN)
