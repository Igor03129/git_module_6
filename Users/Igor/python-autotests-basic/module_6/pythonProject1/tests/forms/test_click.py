from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClick:
    def test_click(self, selenium, new_fixture):
        selenium.get('https://h8xf8u.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.XPATH, '//button/span[contains(text(), "Primary")]').click()

    def test_fail_click(self, selenium):
        selenium.get('https://h8xf8u.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.XPATH, '//button').click()

    def test_double_click(self, selenium):
        selenium.get('https://l8c7w2.csb.app/demo/ToastDemo.html')
        action_chains = webdriver.ActionChains(selenium)
        action_chains.double_click(selenium.find_element(By.XPATH, '//button/span[contains(text(), "Multiple")]'))\
            .perform()

    def test_checkbox(self, selenium):
        selenium.get('https://bn6oef.csb.app/demo/CheckboxDemo.html')
        selenium.find_element(By.CSS_SELECTOR, '[for="city1"]').click()
        selenium.find_element(By.CSS_SELECTOR, '[for="city2"]').click()
        pass

    def test_radio(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://349skk.csb.app/demo/RadioButtonDemo.htl')
        driver.find_element(By.CSS_SELECTOR, '[for="A"]').click()
        pass

    def test_modal(self, setup_up_browser):
        driver = setup_up_browser
        driver.get('https://ghw76z.csb.app/demo/ConfirmDialogDemo.html')
        driver.find_element(By.XPATH, '(//button/span[contains(text(), "Confirm")])[2]').click()
        pass
