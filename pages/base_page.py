import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

from curl import main_site


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=7):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем пока элемент станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, 12).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=7):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=7):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Найти элемент на странице")
    def find_element_on_page(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @allure.step("Найти элементы на странице")
    def find_elements_on_page(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    @allure.step("Ждем когда элемент исчезнет")
    def wait_element_disappear(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        source = self.driver.find_element(*source)
        target = self.driver.find_element(*target)
        drag_and_drop(self.driver, source, target)

    @allure.step('Дождаться появления нужного элемента')
    def wait_for_some_element(self, locator):
        return WebDriverWait(self.driver, timeout=7).until(EC.presence_of_element_located(locator))

    @allure.step('Открыть главную страницу')
    def open_main_site(self):
        self.driver.get(main_site)

