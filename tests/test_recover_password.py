import pytest
import allure

import data
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.recover_password_page import RecoverPasswordPage



class TestRecoverPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_get_recover_password_page_by_button_recover_password(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_enter_to_acc()

        auth_page = AuthPage(driver)
        auth_page.wait_for_auth_page()
        auth_page.click_to_button_recover_password()

        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page_open = recover_password_page.wait_for_recover_password_page()
        assert recover_password_page_open.is_displayed()

    @allure.title('Проверка ввода почты в поле email формы восстановления пароля')
    def test_fill_email_in_password_recover_form(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_enter_to_acc()

        auth_page = AuthPage(driver)
        auth_page.wait_for_auth_page()
        auth_page.click_to_button_recover_password()

        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.wait_for_recover_password_page()
        recover_password_page.fill_email(data.test_email)
        assert recover_password_page.check_text_on_email_field(data.test_email) == True

    @allure.title('Проверка перехода на страницу восстановления пароля после клика на кнопку Восстановить')
    def test_click_to_button_recover(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_enter_to_acc()

        auth_page = AuthPage(driver)
        auth_page.wait_for_auth_page()
        auth_page.click_to_button_recover_password()

        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.wait_for_recover_password_page()
        recover_password_page.fill_email(data.test_email)
        recover_password_page.click_on_button_recover()
        recover_password_page_open = recover_password_page.wait_for_save_recover_password_page()
        assert recover_password_page_open.is_displayed()

    @allure.title('Проверка что поле пароль становится активным при клике по кнопке показать/скрыть пароль')
    def test_click_show_hide_password_focuses_field(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_enter_to_acc()

        auth_page = AuthPage(driver)
        auth_page.wait_for_auth_page()
        auth_page.click_to_button_recover_password()

        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.wait_for_recover_password_page()
        recover_password_page.fill_email(data.test_email)
        recover_password_page.click_on_button_recover()
        recover_password_page.wait_for_save_recover_password_page()
        password_field_focused = recover_password_page.check_password_field_focused_after_click()
        assert password_field_focused == True

