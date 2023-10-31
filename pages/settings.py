from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import Page
from support.logger import logger


class SettingsMenu(Page):

    CHANGE_PASS_BTN = (By.CSS_SELECTOR, 'a[href="/set-new-password"].page-setting-block.w-inline-block')
    # CHANGE_PASS_BTN_MOBILE = (By.XPATH, "//a[contains(@href, '/set-new-password')]")
    # CHANGE_PASS_BTN_MOBILE = (By.CSS_SELECTOR, 'body > div.settings-profile-block > div.settings-block-menu > a:nth-child(11)')
    CHANGE_PASS_BTN_MOBILE = (By.CSS_SELECTOR, 'a[href="/set-new-password"].page-setting-block.w-inline-block')

    def password_change(self):
        # sleep(3)
        self.wait_for_element_clickable_click(self.CHANGE_PASS_BTN)

    def password_change_mobile(self, context):
        # sleep(3)
        actions = ActionChains(context.driver)
        # actions.move_to_element(element).click().perform()
        # WebDriverWait(context.driver, 10).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/set-new-password"].page-setting-block.w-inline-block')))
        for _ in range(5):
            actions.send_keys(Keys.SPACE).perform()
        self.wait_for_element_clickable_click(self.CHANGE_PASS_BTN_MOBILE)

    # ALTERNATIVELY - LAST OPTION !
    # def password_change_mobile(self, context):
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     self.wait_for_element_clickable_click(self.CHANGE_PASS_BTN_MOBILE)
