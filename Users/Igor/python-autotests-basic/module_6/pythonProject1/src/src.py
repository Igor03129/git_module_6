from selenium.webdriver import Chrome, Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions


def run_script():
    Options = ChromeOptions()
    Options.headless = True
    driver = Chrome(options=Options)
    driver.get("https://skillbox.ru")
    assert "Skillbox " == driver.title
    driver.quit()


# driver = Remote(desired_capabilities={
#     "browserName": "chrome",
#     "browserVersion": "latest"
# }, command_executor="http://127.0.0.1:4444/wd/hub")
# driver.get("https://skillbox.ru")
# driver.quit()

# if __name__ == '__main__':
#     run_script()
