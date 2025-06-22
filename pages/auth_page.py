from pages.base_page import BasePage
import allure
from locators.auth_page_locators import AuthPageLocators


class AuthPage(BasePage):
    @allure.step('Подождать загрузку страницы')
    def wait_for_auth_page(self):
        self.wait_for_element(AuthPageLocators.AUTH_PAGE, 15)
        self.wait_for_element_hide(AuthPageLocators.OVERLAY)
        return self.find_element_on_page(AuthPageLocators.AUTH_PAGE)

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_to_button_recover_password(self):
        self.click_on_element(AuthPageLocators.RECOVER_PASSWORD)

    @allure.step('Заполнить форму авторизации')
    def fill_auth_form(self, email, password):
        self.send_keys_to_input(AuthPageLocators.EMAIL, email)
        self.send_keys_to_input(AuthPageLocators.PASSWORD, password)

    @allure.step('Нажать на кнопку Войти в форме авторизации')
    def click_to_enter_button_for_auth(self):
        self.wait_for_element_hide(AuthPageLocators.OVERLAY)
        self.wait_for_element(AuthPageLocators.ENTER_BUTTON)
        self.click_on_element(AuthPageLocators.ENTER_BUTTON)

    @allure.step('Нажать на кнопку Конструктор')
    def click_to_constructor_button(self):
        self.click_on_element(AuthPageLocators.CONSTRUCTOR)

