import pytest
import allure

import data
from pages.auth_page import AuthPage
from pages.main_page import MainPage


class TestConstructor:
    @allure.title("Проверка перехода в Конструктор со страницы авторизации")
    def test_switch_to_constructor_from_auth_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_enter_to_personal_acc()

        auth_page = AuthPage(driver)
        auth_page.wait_for_auth_page()
        auth_page.click_to_constructor_button()

        constructor = main_page.wait_for_constructor()
        assert constructor.is_displayed()

    @allure.title('Проверка открытия окна с информацией об ингредиенте')
    @pytest.mark.parametrize('ingredient', data.INGREDIENTS)
    def test_open_info_window_of_ingredient_by_click(self, driver, ingredient):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_ingredient(ingredient)
        ingredient_info_window_open = main_page.check_window_info_of_ingredient_open()
        assert ingredient_info_window_open.is_displayed()

    @allure.title('Проверка закрытия окна с информацией об ингредиенте')
    @pytest.mark.parametrize('ingredient', data.INGREDIENTS)
    def test_close_info_window_of_ingredient(self, driver, ingredient):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_ingredient(ingredient)
        main_page.check_window_info_of_ingredient_open()
        ingredient_info_window_close = main_page.close_window_info_of_ingredient()
        assert ingredient_info_window_close == True

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении ингредиента в заказ')
    def test_ingredient_count_increase_when_ingredient_add(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        ingredient1_increased, ingredient2_increased, ingredient3_increased = (
            main_page.check_counter_increasing_when_ingredient_add())
        assert ingredient1_increased == True
        assert ingredient2_increased == True
        assert ingredient3_increased == True

