from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest
import time

# ссылки
link = "http://selenium1py.pythonanywhere.com/accounts"  # ссылка на главную
loginlink = "http://selenium1py.pythonanywhere.com/accounts/login/"  # ссылка на страницу с логином
productlink = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"  # ссылка на страницу с товаром
# логин и пароль для регистрации
email = str(time.time()) + "@fakemail.org"
password = '1a3b5c7d9'


# пользователь может добавить в корзину
class TestUserAddToBasketFromProductPage:
    # создаем нового пользователя
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, loginlink)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    # нет сообщения об успехе при добавлении товара в корзину (элемент не появляется в течении заданного времени)
    @pytest.mark.xfail
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, productlink)
        page.open()
        page.add_product_to_basket()  # добавление продукта в корзину
        page.should_not_be_success_message()

    # добавление товара, в корзине тот же товар, цена совпадает
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, productlink)
        page.open()
        page.add_product_to_basket()  # добавление продукта в корзину
        page.should_be_item_in_basket()  # добавился тот же товар
        page.should_be_price_in_basket()  # цена совпадает с добавленным товаром


# нет сообщения об успехе при добавлении товара в корзину (#элемент исчезает)

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, productlink)
    page.open()
    page.add_product_to_basket()  # добавление продукта в корзину
    page.should_be_disappeared_message()


# гость может добавить в корзину
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, productlink)
    page.open()
    page.add_product_to_basket()  # добавление продукта в корзину
    page.should_be_item_in_basket()  # добавился тот же товар
    page.should_be_price_in_basket()  # цена совпадает с добавленным товаром


# гость может видеть ссылку на страницу с логином

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, productlink)
    page.open()
    page.should_be_login_link()


# гость может перейти на страницу с логином из страницы с товаром
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, productlink)
    page.open()
    page.go_to_login_page()


# гость может перейти в корзину и увидеть там товар(ы)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.products_in_basket()
    page.basket_text()
