from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest #чтобы работали маркированные тесты


# main_page

# гостевой пользователь может попасть на страницу логина

class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

    # гостевой пользователь может увидеть ссылку на страницу логина
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()


# login_page

# подстрока "login" есть в текущем url браузера
# присутствует форма регистрации
# пристутсвует форма логина
@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# гость может перейти в корзину и увидеть там товар(ы)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.products_in_basket()
    page.basket_text()

