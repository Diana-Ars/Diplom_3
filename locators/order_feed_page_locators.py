import pytest
from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_PAGE = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    FIRST_ORDER_IN_ORDER_LIST = By.XPATH, ('//ul[contains(@class, "OrderFeed_list__OLh59")]'
                                           '/li[contains(@class, "OrderHistory_listItem__2x95r mb-6")][1]')
    ORDER_INFO = By.XPATH, '//p[contains(text(), "Cостав")]'
    COMPLETED_IN_ALL_TIME = (By.XPATH,
    '//div[(@class="undefined mb-15")]/p[(@class="OrderFeed_number__2MbrQ text text_type_digits-large")]')
    COMPLETED_IN_TODAY = (By.XPATH, '//div[contains(., "Выполнено за сегодня:")]'
                                    '/p[contains(@class, "OrderFeed_number__2MbrQ text text_type_digits-large")]')
    ORDER_IN_WORK = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi")]'
                               '/li[contains(@class, "text text_type_digits-default mb-2")]')


    @staticmethod
    def get_order_by_number(order_number):
        return (By.XPATH, f'//p[contains(@class, "text text_type_digits-default") and text()="{order_number}"]')

