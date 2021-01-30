from .pages.main_page import MainPage
from .pages.locators import Urls
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)    # инициализируем Page Object, передаем в конструктор
                                                             # экземпляр драйвера и url адрес
        main_page.open()                                     # открываем страницу
        main_page.go_to_login_page()                         # выполняем метод страницы — переходим на страницу логина

        # переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page = MainPage(browser, Urls.MAIN_PAGE_URL)
        main_page.open()
        main_page.should_be_basket_link()
        main_page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.basket_should_be_empty()
        basket_page.should_be_message_that_basket_is_empty()
