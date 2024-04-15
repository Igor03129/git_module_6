import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# from src.actions.components.forms import fill_forms
# from src.helpers.accounts_base import AccountsBase

@allure.feature('Full Accounts')
@allure.story('Waiting page load')
class TestAsyncWait(AccountsBase):
    @allure.title('Проверка загрузки страницы')
    def test_wait_page_load(self, selenium, go_to_github):
        with allure.step('Ожидание сообщения "build from here"'):
            selenium.find_element(By.XPATH, '//*[contains(text(), "build from here")]')

    def test_wait_types(self, selenium, go_to_github):
        #selenium.find_element(By.XPATH, '//*[contains(text(), "build from here")]')
        WebDriverWait(selenium, timeout=3).until(
            lambda d: d.find_element(By.XPATH, '//*[contains(text(), "build from here")]')
        )

    def test_wait_dialog(self, selenium):
        with allure.step('Открытие страницы https://m1vcki.csb.app/'):
            selenium.get('https://m1vcki.csb.app/')

        with allure.step('Ожидание отображения формы'):
            WebDriverWait(selenium, timeout=30).until(lambda d: d.find_element(By.ID, 'name'))

        with allure.step('Заполнение формы данных'):
            fill_forms(selenium, name="awesome_skillbox")

        #selenium.find_element(By.XPATH, '//*[contains(text(), "build from here")]')
        with allure.step('Ожидание отображения диалогового окна'):
            WebDriverWait(selenium, timeout=5).until(
                lambda d: d.find_element(By.XPATH, '//button/span[contains(text(), "OK")]')
            )
        with allure.step('Клик по кнопке OK'):
            selenium.find_element(By.XPATH, '//button/span[contains(text(), "OK")]').click()
