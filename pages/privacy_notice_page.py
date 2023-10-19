from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class PrivacyNoticePage(Page):
    PRIVACY_NOTICE_LINK = (By.XPATH, "//a[contains(@href, '/privacy')]")

    def open_amazon_tc_page(self):
        self.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref'
                        '=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
        sleep(2)
        self.driver.refresh()

    def store_original_window(self):
        return self.get_current_window()
        # print("Current window", self.get_current_window())
        # print("All windows", self.get_windows())

    def click_privacy_notice_link(self):
        self.click(*self.PRIVACY_NOTICE_LINK)

    def verify_opened(self):
        self.verify_partial_url('/display.html?nodeId=GX7NJQ4ZB8MHFRNJ')

