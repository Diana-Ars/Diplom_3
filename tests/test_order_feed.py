import pytest
import allure

from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from curl import main_site


class TestOrderFeed:
    @allure.title('Проверка перехода в раздел Лента заказов с главной страницы')
    def test_switch_to_order_feed_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_order_feed()

        order_feed = OrderFeedPage(driver)
        order_feed_open = order_feed.wait_for_order_feed_page()
        assert order_feed_open.is_displayed()

    @allure.title('Проверка открывания всплывающего окна с деталями при клике на заказ в Ленте заказов')
    def test_open_window_order_info_by_click_to_order(self, driver, login_user_and_create_order):
        driver.get(main_site)
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_order_feed()

        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_page()
        order_feed.click_on_order_in_order_feed()
        order_info_window_open = order_feed.check_order_info_window_open_when_click_to_order_in_order_list()
        assert order_info_window_open == True

    @allure.title('Проверка что заказы из Истории заказов пользователя отображаются в Ленте заказов')
    def test_orders_in_history_orders_are_presence_in_order_feed(self, driver, get_order_numbers_from_history):
        driver.get(main_site)
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_order_feed()

        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_page()
        presence_in_order_feed = order_feed.check_some_orders_presence_in_order_feed(get_order_numbers_from_history)
        assert presence_in_order_feed == True

    @allure.title('Проверка что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_completed_in_all_time_increment_when_order_create(self, driver, login_user_and_create_order):
        order_number, previous_count_all_time, previous_count_today = login_user_and_create_order
        driver.get(main_site)
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_order_feed()

        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_page()
        current_count_text = order_feed.check_count_completed_in_all_time()
        current_count = int(current_count_text)
        assert current_count > previous_count_all_time

    @allure.title('Проверка что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_completed_in_today_increment_when_order_create(self, driver, login_user_and_create_order):
        order_number, previous_count_all_time, previous_count_today = login_user_and_create_order
        driver.get(main_site)
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_order_feed()

        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_page()
        current_count_text = order_feed.check_count_completed_in_today()
        current_count = int(current_count_text)
        assert current_count > previous_count_today

    @allure.title('Проверка что текущий заказ отображается в списке В работе')
    def test_current_order_presence_in_order_in_work(self, driver, login_user_and_create_order):
        order_number, previous_count_all_time, previous_count_today = login_user_and_create_order
        order_number_formated = f'0{order_number}'
        driver.get(main_site)
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_to_button_order_feed()

        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_page()
        current_order_in_work = order_feed.check_order_presence_in_order_in_work(order_number_formated)
        assert current_order_in_work == True

