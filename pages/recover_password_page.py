from pages.base_page import BasePage
import allure
from locators.recover_password_page_locators import RecoverPasswordPageLocators


class RecoverPasswordPage(BasePage):
    @allure.step('Подождать загрузку страницы восстановления пароля')
    def wait_for_recover_password_page(self):
        self.wait_for_element(RecoverPasswordPageLocators.RECOVER_PASSWORD_PAGE, 15)
        self.wait_for_element_hide(RecoverPasswordPageLocators.OVERLAY)
        return self.find_element_on_page(RecoverPasswordPageLocators.RECOVER_PASSWORD_PAGE)

    @allure.step('Ввести значение в поле email')
    def fill_email(self, email):
        self.click_on_element(RecoverPasswordPageLocators.EMAIL_FIELD)
        self.send_keys_to_input(RecoverPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_on_button_recover(self):
        self.click_on_element(RecoverPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Подождать загрузку страницы с указанием пароля')
    def wait_for_save_recover_password_page(self):
        self.wait_for_element(RecoverPasswordPageLocators.SAVE_RECOVER_PASSWORD, 15)
        self.wait_for_element_hide(RecoverPasswordPageLocators.OVERLAY)
        return self.find_element_on_page(RecoverPasswordPageLocators.SAVE_RECOVER_PASSWORD)

    @allure.step('Нажать на кнопку показать/скрыть пароль')
    def click_on_button_to_visible_password(self):
        self.click_on_element(RecoverPasswordPageLocators.PASSWORD_VIEW)

    @allure.step('Проверить что в поле email вводится почта')
    def check_text_on_email_field(self, email):
        email_input = self.find_element_on_page(RecoverPasswordPageLocators.EMAIL_INPUT)
        actual_text = email_input.get_attribute('value')
        return actual_text == email

    @allure.step('Проверить что поле пароля подсвечивается при нажатии на кнопку показать/скрыть пароль')
    def check_password_field_focused_after_click(self):
        self.click_on_element(RecoverPasswordPageLocators.PASSWORD_VIEW)
        self.wait_for_element_hide(RecoverPasswordPageLocators.OVERLAY)
        self.wait_for_some_element(RecoverPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
        expected_result = self.find_element_on_page(RecoverPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
        return expected_result.is_displayed()

