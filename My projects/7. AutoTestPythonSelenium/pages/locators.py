from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_TEXT = (By.TAG_NAME, "p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN = (By.NAME, "registration-email")
    PASSWORD1 = (By.NAME, "registration-password1")
    PASSWORD2 = (By.NAME, "registration-password2")
    REG_USER = (By.NAME, "registration_submit")
    REG_OK = (By.CSS_SELECTOR, ".icon-ok-sign")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    EXPECTED_ITEM_IN_BASKET = (By.TAG_NAME, 'h1:nth-child(1)')
    ACTUAL_ITEM_IN_BASKET = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    EXPECTED_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ACTUAL_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
