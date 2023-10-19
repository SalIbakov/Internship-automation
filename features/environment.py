from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application
from support.logger import logger


def browser_init(context):
    """
    :param context: Behave context
    """
    options = Options()
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    options.add_argument('--ignore-certificate-errors')
    # service = Service(executable_path=r'C:\Users\Admin\Downloads\python-selenium-automation-main\internship-automation\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)

    # --- FIREFOX cross-browser test --- #
    # service = Service(executable_path=r'C:\Users\Admin\Downloads\python-selenium-automation-main\internship-automation\geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, 10)

    # context.app = Application(context.driver)

    # --- HEADLESS MODE --- #
    options = webdriver.ChromeOptions()
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1000,1000')
    service = Service(executable_path=r'C:\Users\Admin\Downloads\python-selenium-automation-main\internship-automation\chromedriver.exe')
    context.driver = webdriver.Chrome(
        options=options,
        service=service
     )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
