import pytest
from selenium.webdriver.common.by import By


class RecoverPasswordPageLocators:
    RECOVER_PASSWORD_PAGE = By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]"
    EMAIL_FIELD = By.XPATH, "//div[contains(@class, 'input pr-6 pl-6 input_type_text input_size_default')]"
    EMAIL_INPUT = By.XPATH, "//input[contains(@class, 'text input__textfield text_type_main-default')]"
    RECOVER_BUTTON = By.XPATH, "//button[contains(text(), 'Восстановить')]"
    PASSWORD_FIELD = By.CLASS_NAME, 'input pr-6 pl-6 input_type_password input_size_default'
    PASSWORD_VIEW = (By.XPATH, "//div[contains(@class, 'input__icon input__icon-action')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
    SAVE_RECOVER_PASSWORD = By.XPATH, "//button[contains(text(), 'Сохранить')]"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"

