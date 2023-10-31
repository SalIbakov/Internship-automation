from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# EMAIL_FIELD = (By.ID, 'email-2')
# PASSWORD_FIELD = (By.ID, 'field')
# LOG_IN_BUTTON = (By.CSS_SELECTOR, 'a.login-button.w-button')
# CHANGE_PASS_BTN_MOBILE = (By.CSS_SELECTOR, 'a[href="/set-new-password"].page-setting-block.w-inline-block')


@given('Open Main Log In page')
def open_login_page(context):
    # context.app.log_in_page.open_login_page()
    context.driver.get('https://soft.reelly.io/sign-in')


@when('Log in to the page')
def page_log_in(context):
    context.app.log_in_page.page_log_in()


@then('Click on settings option')
def click_settings(context):
    context.app.main_page.click_settings()


@then('Click on settings option in Mobile')
def click_settings_mobile(context):
    sleep(3)
    context.app.main_page.click_settings_mobile()


@then('Click on Change password option')
def password_change(context):
    context.app.settings.password_change()


@then('Click on Change password option in Mobile')
def password_change_mobile(context):
    # context.driver.find_element(*CHANGE_PASS_BTN_MOBILE)
    context.app.settings.password_change_mobile(context)


@then('Verify the right page opens')
def correct_page_open(context):
    context.app.main_page.correct_page_open()


@then('Add some test password to the input fields')
def input_text_field(context):
    context.app.log_in_page.input_text_field()


@then('Verify the “Change password” button is available')
def verify_btn_available(context):
    context.app.main_page.verify_btn_available()
