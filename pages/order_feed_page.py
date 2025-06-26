from pages.base_page import BasePage
import allure
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    @allure.step('Подождать загрузку страницы с Лентой заказов')
    def wait_for_order_feed_page(self):
        self.wait_for_element(OrderFeedPageLocators.ORDER_FEED_PAGE)
        self.wait_for_element_hide(OrderFeedPageLocators.OVERLAY)
        return self.find_element_on_page(OrderFeedPageLocators.ORDER_FEED_PAGE)

    @allure.step('Нажать на заказ в Ленте заказов')
    def click_on_order_in_order_feed(self):
        self.click_on_element(OrderFeedPageLocators.FIRST_ORDER_IN_ORDER_LIST)

    @allure.step('Проверить что открылось окно с деталями заказа при нажатии на него')
    def check_order_info_window_open_when_click_to_order_in_order_list(self):
        self.wait_for_element_hide(OrderFeedPageLocators.OVERLAY)
        self.find_element_on_page(OrderFeedPageLocators.ORDER_INFO)
        return True

    @allure.step('Проверить что конкретные заказы отображаются в Ленте заказов')
    def check_some_orders_presence_in_order_feed(self, order_numbers):
        for number in order_numbers:
            self.find_element_on_page(OrderFeedPageLocators.get_order_by_number(number))
            return True

    @allure.step('Посмотреть значение счетчика Выполнено за все время')
    def check_count_completed_in_all_time(self):
        count = self.find_element_on_page(OrderFeedPageLocators.COMPLETED_IN_ALL_TIME)
        return count.text

    @allure.step('Посмотреть значение счетчика Выполнено за сегодня')
    def check_count_completed_in_today(self):
        count = self.find_element_on_page(OrderFeedPageLocators.COMPLETED_IN_TODAY)
        return count.text

    @allure.step('Проверить что конкретный заказ отображается в списке В работе')
    def check_order_presence_in_order_in_work(self, order_number):
        self.wait_for_some_element(OrderFeedPageLocators.ORDER_IN_WORK)
        orders_in_work = self.find_elements_on_page(OrderFeedPageLocators.ORDER_IN_WORK)
        orders_in_work_texts = [order.text for order in orders_in_work]
        if order_number in orders_in_work_texts:
            return True

