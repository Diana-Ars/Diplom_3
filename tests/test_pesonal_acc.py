import pytest
import allure

from curl import main_site
from pages.auth_page import AuthPage
from pages.personal_acc_page import PersonalAccPage
from pages.main_page import MainPage


class TestPersonalAcc:
    @allure.title('Проверка перехода в личный кабинет с главной страницы')
    def test_enter_to_personal_acc_from_main_page(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.open_main_site()
        main_page.wait_for_main_page()
        main_page.click_to_button_enter_to_personal_acc()

        personal_acc_page = PersonalAccPage(driver)
        personal_acc_open = personal_acc_page.wait_for_personal_acc_page()
        assert personal_acc_open.is_displayed()

    @allure.title('Проверка перехода в раздел История заказов')
    def test_switch_to_orders_history_from_main_page(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.open_main_site()
        main_page.wait_for_main_page()
        main_page.click_to_button_enter_to_personal_acc()

        personal_acc_page = PersonalAccPage(driver)
        personal_acc_page.wait_for_personal_acc_page()
        orders_history_open = personal_acc_page.switch_to_orders_history()
        assert orders_history_open.is_displayed()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.open_main_site()
        main_page.wait_for_main_page()
        main_page.click_to_button_enter_to_personal_acc()

        personal_acc_page = PersonalAccPage(driver)
        personal_acc_page.wait_for_personal_acc_page()
        personal_acc_page.click_logout_button()

        auth_page = AuthPage(driver)
        user_logout = auth_page.wait_for_auth_page()
        assert user_logout.is_displayed()

