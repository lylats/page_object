from selenium.webdriver.common.by import By


class Urls():
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/accounts/login"
    LINK1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    LINK2 = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    PROMO_LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ALERT_THAT_PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LOCATOR = (By.CSS_SELECTOR, ".basket-mini > span > .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_LOCATOR = (By.CSS_SELECTOR, "#content_inner > p")
