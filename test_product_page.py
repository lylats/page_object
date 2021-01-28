import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.locators import Urls
from pages.basket_page import BasketPage

pytest_params = [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)]


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', pytest_params)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_product_name_and_price()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_alert_that_product_add_to_basket()
    product_page.is_product_price_the_same()
    product_page.is_product_name_the_same()


@pytest.mark.xfail(reason="guest see message after adding")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, Urls.PROMO_LINK)
    product_page.open()

    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, Urls.PROMO_LINK)
    product_page.open()

    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="succes message doesnt dissapear")
def test_message_dissapeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, Urls.PROMO_LINK)
    product_page.open()

    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.success_message_should_dissapear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Urls.LINK2)
    page.open()

    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, Urls.LINK2)
    product_page.open()

    product_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, Urls.LINK2)
    product_page.open()

    product_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_be_message_that_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, Urls.LOGIN_PAGE_URL)
        login_page.open()

        new_user_email = str(time.time()) + "@fakemail.org"
        new_user_password = 'FakePassword'

        login_page.register_new_user(new_user_email, new_user_password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, Urls.LINK1)
        product_page.open()

        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, Urls.LINK1)
        product_page.open()

        product_page.should_be_product_name_and_price()
        product_page.add_product_to_basket()
        product_page.should_be_alert_that_product_add_to_basket()
        product_page.is_product_price_the_same()
        product_page.is_product_name_the_same()
