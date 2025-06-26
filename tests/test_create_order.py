import pytest
import allure

from curl import main_site
from pages.main_page import MainPage


class TestCreateOrder:
    @allure.title('Проверка успешного оформления заказа авторизованным пользователем')
    def test_create_order_by_auth_user(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.open_main_site()
        main_page.wait_for_main_page()
        main_page.click_to_button_create_order()
        create_order = main_page.wait_for_creating_order_window()
        assert create_order

