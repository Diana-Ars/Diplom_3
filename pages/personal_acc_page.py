from pages.base_page import BasePage
import allure
from locators.personal_acc_page_locators import PersonalAccPageLocators


class PersonalAccPage(BasePage):
    @allure.step('Подождать загрузку страницы Личного кабинета')
    def wait_for_personal_acc_page(self):
        self.wait_for_element(PersonalAccPageLocators.PERSONAL_ACC)
        self.wait_for_element_hide(PersonalAccPageLocators.OVERLAY)
        return self.find_element_on_page(PersonalAccPageLocators.PERSONAL_ACC)

    @allure.step('Перейти в раздел История заказов')
    def switch_to_orders_history(self):
        self.wait_for_element_hide(PersonalAccPageLocators.OVERLAY)
        self.click_on_element(PersonalAccPageLocators.ORDERS_HISTORY)
        return self.find_element_on_page(PersonalAccPageLocators.ORDERS_HISTORY_ACTIVE)

    @allure.step('Нажать на кнопку Выход в Личном кабинете')
    def click_logout_button(self):
        self.wait_for_element_hide(PersonalAccPageLocators.OVERLAY)
        self.click_on_element(PersonalAccPageLocators.LOGOUT_BUTTON)

    @allure.step('Подождать загрузку списка истории заказов')
    def wait_for_order_history_list(self):
        self.wait_for_element(PersonalAccPageLocators.ORDERS_HISTORY_LIST)

