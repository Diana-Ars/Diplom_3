from pages.base_page import BasePage
import allure

from locators.main_page_locators import *


class MainPage(BasePage):
    @allure.step('Подождать загрузку страницы')
    def wait_for_main_page(self):
        self.wait_for_element(MainPageLocators.MAIN_PAGE, 10)
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        return self.find_element_on_page(MainPageLocators.MAIN_PAGE)

    @allure.step('Нажать на кнопку "Войти в аккаунт"')
    def click_to_button_enter_to_acc(self):
        self.click_on_element(MainPageLocators.ENTER_TO_ACC)

    @allure.step('Нажать на кнопку Личный кабинет')
    def click_to_button_enter_to_personal_acc(self):
        self.click_on_element(MainPageLocators.ENTER_TO_PERSONAL_ACC)

    @allure.step('Подождать загрузку Конструктора')
    def wait_for_constructor(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR)
        return self.find_element_on_page(MainPageLocators.CONSTRUCTOR)

    @allure.step('Нажать на кнопку Лента заказов')
    def click_to_button_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED)

    @allure.step('Нажать на ингредиент')
    def click_to_ingredient(self, ingredient):
        ingredient_locator = ConstructorLocators.choose_ingredient(ingredient)
        self.scroll_to_element(ingredient_locator)
        self.click_on_element(ingredient_locator)

    @allure.step('Проверить открытие окна с информацией об ингредиенте')
    def check_window_info_of_ingredient_open(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.wait_for_element(ConstructorLocators.INGREDIENT_INFO)
        return self.find_element_on_page(ConstructorLocators.INGREDIENT_INFO)

    @allure.step('Закрыть окно с информацией об ингредиенте')
    def close_window_info_of_ingredient(self):
        self.click_on_element(ConstructorLocators.CLOSE_INGREDIENT_INFO)
        self.wait_element_disappear(ConstructorLocators.INGREDIENT_INFO)
        return True

    @allure.step('Перенести ингредиенты в заказ')
    def put_ingredients_in_order(self):
        self.drag_and_drop_element(ConstructorLocators.INGREDIENT_SOURCE_1, ConstructorLocators.INGREDIENT_TARGET)
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.drag_and_drop_element(ConstructorLocators.INGREDIENT_SOURCE_2, ConstructorLocators.INGREDIENT_TARGET)
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.drag_and_drop_element(ConstructorLocators.INGREDIENT_SOURCE_3, ConstructorLocators.INGREDIENT_TARGET)
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_count(self, counter_locator):
        ingredient_count = self.find_element_on_page(counter_locator)
        return int(ingredient_count.text)

    @allure.step('Проверить что счетчик ингредиента увеличивается при его добавлении в заказ')
    def check_counter_increasing_when_ingredient_add(self):
        previous_count_1 = self.get_ingredient_count(ConstructorLocators.INGREDIENT_COUNTER_1)
        previous_count_2 = self.get_ingredient_count(ConstructorLocators.INGREDIENT_COUNTER_2)
        previous_count_3 = self.get_ingredient_count(ConstructorLocators.INGREDIENT_COUNTER_3)
        self.put_ingredients_in_order()
        actual_count_1 = self.get_ingredient_count(ConstructorLocators.INGREDIENT_COUNTER_1)
        actual_count_2 = self.get_ingredient_count(ConstructorLocators.INGREDIENT_COUNTER_2)
        actual_count_3 = self.get_ingredient_count(ConstructorLocators.INGREDIENT_COUNTER_3)
        ingredient1_increased = actual_count_1 > previous_count_1
        ingredient2_increased = actual_count_2 > previous_count_2
        ingredient3_increased = actual_count_3 > previous_count_3
        return ingredient1_increased, ingredient2_increased, ingredient3_increased

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_to_button_create_order(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Подождать загрузку окна после оформления заказа')
    def wait_for_creating_order_window(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.wait_for_element(MainPageLocators.ORDER_CREATING)
        return True

    @allure.step('Получить номер оформленного заказа')
    def get_order_number(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
        self.wait_element_disappear(MainPageLocators.ORDER_NUMBER_OVERLAY)
        order_number = self.find_element_on_page(MainPageLocators.ORDER_NUMBER)
        return int(order_number.text)

