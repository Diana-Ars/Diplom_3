import pytest
from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = By.XPATH, "//h1[contains(@class, 'text text_type_main-large mb-5 mt-10')]"
    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    ENTER_TO_ACC = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    ENTER_TO_PERSONAL_ACC = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
    CONSTRUCTOR = By.XPATH, '//h1[contains(text(), "Соберите бургер")]'
    ORDER_FEED = By.XPATH, '//p[contains(text(), "Лента Заказов")]'
    CREATE_ORDER_BUTTON = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"
    ORDER_CREATING = (By.XPATH,
        '//div[contains(@class, "Modal_modal__container__Wo2l_")]//p[contains(text(), "Ваш заказ начали готовить")]')
    ORDER_NUMBER = (By.XPATH,
    '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    ORDER_NUMBER_OVERLAY = (By.XPATH, '//h2[contains(text(), "9999")]')

class ConstructorLocators:
    INGREDIENT_INFO = (By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]'
     '/div[contains(@class, "Modal_modal__container__Wo2l_")]')
    CLOSE_INGREDIENT_INFO = (By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]'
    '//button[contains(@class, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")]')
    INGREDIENT_SOURCE_1 = (By.CSS_SELECTOR,
    'ul.BurgerIngredients_ingredients__list__2A-mT:nth-child(2) > a:nth-child(2) > img:nth-child(2)')
    INGREDIENT_SOURCE_2 = (By.XPATH,
                            '//img[contains(@alt, "Соус с шипами Антарианского плоскоходца") and '
                            '@class="BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4"]')
    INGREDIENT_SOURCE_3 = (By.XPATH,
                           '//img[contains(@alt, "Говяжий метеорит (отбивная)") and '
                           '@class="BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4"]')
    INGREDIENT_TARGET = (By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7')
    INGREDIENT_COUNTER_1 = (By.XPATH,
                    '//a[.//img[@alt="Краторная булка N-200i"]]//p[contains(@class, "counter_counter__num__3nue1")]')
    INGREDIENT_COUNTER_2 = (By.XPATH,
                            '//a[.//img[@alt="Соус с шипами Антарианского плоскоходца"]]'
                            '//p[contains(@class, "counter_counter__num__3nue1")]')
    INGREDIENT_COUNTER_3 = (By.XPATH,
                            '//a[.//img[@alt="Говяжий метеорит (отбивная)"]]'
                            '//p[contains(@class, "counter_counter__num__3nue1")]')

    @staticmethod
    def choose_ingredient(ingredient):
        return By.XPATH, f'//p[contains(text(), "{ingredient}")]'

