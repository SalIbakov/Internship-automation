from pages.main_page import MainPage
from pages.log_in_page import LoginPage
from pages.settings import SettingsMenu


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.log_in_page = LoginPage(driver)
        self.settings = SettingsMenu(driver)

