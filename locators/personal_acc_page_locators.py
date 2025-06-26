import pytest
from selenium.webdriver.common.by import By


class PersonalAccPageLocators:
    PERSONAL_ACC = (By.XPATH, '//a[contains(text(), "Профиль")]')
    ORDERS_HISTORY = By.XPATH, '//a[contains(text(), "История заказов")]'
    ORDERS_HISTORY_ACTIVE = (By.XPATH, '//a[contains(@class, "Account_link_active")]')
    LOGOUT_BUTTON = By.XPATH, '//button[contains(text(), "Выход")]'
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    ORDERS_HISTORY_LIST = By.XPATH, '//ul[contains(@class, "OrderHistory_profileList__374GU OrderHistory_list__KcLDB")]'

    @staticmethod
    def get_orders_numbers_from_history(driver):
        history_orders_locator = (By.XPATH, '//ul[contains(@class, "OrderHistory_profileList__374GU OrderHistory_list__KcLDB")]/li')
        history_elements = driver.find_elements(*history_orders_locator)
        order_numbers = []
        for element in history_elements:
            try:
                number_element = element.find_element(By.XPATH,
                                                      './/p[contains(@class, "text text_type_digits-default")]')
                order_numbers.append(number_element.text.strip())
            except:
                continue
        return order_numbers

