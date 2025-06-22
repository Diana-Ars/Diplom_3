import pytest
import requests
import time

import curl
from curl import *
from selenium import webdriver
from faker import Faker
import uuid
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.personal_acc_page import PersonalAccPage
from pages.order_feed_page import OrderFeedPage
from locators.personal_acc_page_locators import PersonalAccPageLocators


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    yield driver
    driver.quit()



@pytest.fixture                       # Фикстура для создания пользователя
def create_user(driver):
    fake = Faker()
    unique_login = str(uuid.uuid4())
    user_data = {
        "email": f"test_{unique_login}@{fake.domain_name()}",
        "password": fake.password(),
        "name": f"user_{unique_login}"
    }
    creation = requests.post(curl.url_create_user, json=user_data)
    print(creation.json())
    if creation.status_code != 200:
        creation = requests.post(curl.url_create_user, json=user_data)
    assert creation.status_code == 200
    token = creation.json().get('accessToken')
    user = {
        'email': user_data['email'],
        'name': user_data['name'],
        'password': user_data['password'],
        'accessToken': token,
        'headers': {
            'Authorization': token
        }
    }
    yield user
    delete_user = requests.delete(curl.url_delete_user, headers={'Authorization': token})
    print(delete_user.json())

@pytest.fixture
def login_user(driver, create_user):               # Фикстура для авторизации пользователя
    user = create_user
    main_page = MainPage(driver)
    main_page.wait_for_main_page()
    main_page.click_to_button_enter_to_acc()

    auth_page = AuthPage(driver)
    auth_page.fill_auth_form(email=user['email'], password=user['password'])
    auth_page.click_to_enter_button_for_auth()
    main_page.wait_for_main_page()
    return driver

@pytest.fixture     # Получение значение счетчиков Заказы за все время и Заказы за сегодня
def check_previous_count_of_orders(driver):
    main_page = MainPage(driver)
    main_page.wait_for_main_page()
    main_page.click_to_button_order_feed()

    order_feed = OrderFeedPage(driver)
    order_feed.wait_for_order_feed_page()
    previous_count_all_time = order_feed.check_count_completed_in_all_time()
    previous_count_today = order_feed.check_count_completed_in_today()
    return int(previous_count_all_time), int(previous_count_today)

@pytest.fixture      # Фикстура для создания заказа авторизованного пользователя
def login_user_and_create_order(driver, login_user, check_previous_count_of_orders):
    # Предварительно получаем значение счетчиков Заказы за все время и Заказы за сегодня
    previous_count_all_time, previous_count_today = check_previous_count_of_orders
    driver.get(main_site)

    main_page = MainPage(driver)
    main_page.wait_for_main_page()
    main_page.put_ingredients_in_order()
    main_page.click_to_button_create_order()
    order_number = main_page.get_order_number()
    # Возвращаем номер созданного заказа, изначальное значение счетчиков Заказы за все время и Заказы за сегодня
    return order_number, previous_count_all_time, previous_count_today

@pytest.fixture   # Фикстура для получения номеров заказов авторизованного пользователя из Истории заказов
def get_order_numbers_from_history(driver, login_user_and_create_order):
    driver.get(main_site)
    main_page = MainPage(driver)
    main_page.wait_for_main_page()
    main_page.put_ingredients_in_order()
    main_page.click_to_button_create_order()
    driver.get(main_site)
    main_page = MainPage(driver)
    main_page.wait_for_main_page()
    main_page.click_to_button_enter_to_personal_acc()

    personal_acc_page = PersonalAccPage(driver)
    personal_acc_page.switch_to_orders_history()
    personal_acc_page.wait_for_order_history_list()
    order_numbers = PersonalAccPageLocators.get_orders_numbers_from_history(driver)
    return order_numbers

