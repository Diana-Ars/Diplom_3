import pytest
from selenium.webdriver.common.by import By


class AuthPageLocators:
    AUTH_PAGE = By.XPATH, "//h2[contains(text(), 'Вход')]"
    RECOVER_PASSWORD = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"
    EMAIL = By.XPATH, "//input[contains(@name, 'name')]"
    PASSWORD = By.XPATH, "//input[contains(@name, 'Пароль')]"
    ENTER_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    CONSTRUCTOR = By.XPATH, '//p[contains(text(), "Конструктор")]'

