import pytest
from selenium.webdriver.chrome.options import Options
import logging

# class Remote:
#     pass


@pytest.fixture()
def selenium(pytestconfig):

    options = Options()
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f'Prepare{browser_name} browser...')
    if pytestconfig.getini("headless") == 'True' and browser_name == "chrome":
        options.add_argument("--headless")
    driver = Remote(
        desired_capabilities={
            "browserName": pytestconfig.getini("browser_name")
            "browserVersion": pytestconfig.getini("browser_version")
        },
        command_executor=pytestconfig.getini("selenium_url"),
        optios=options
    )
    logging.info(f'Browser{browser_name} has been started')
    yield driver
    driver.quit()