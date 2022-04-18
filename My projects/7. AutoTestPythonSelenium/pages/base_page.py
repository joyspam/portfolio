from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    # метод, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # элемент появляется на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # будет ждать до тех пор, пока элемент не исчезнет:
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

# методы для всех страниц

    # переход в корзину со страниц
    def go_to_basket(self):
        assert self.is_element_present(*BasePageLocators.GO_TO_BASKET), "No link to basket or invalid selector"
        go_to_basket = self.browser.find_element(*BasePageLocators.GO_TO_BASKET)
        go_to_basket.click()

    # переход на страницу логина со страниц
    def go_to_login_page(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "You should change LOGIN_LINK_INVALID"
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # можно видеть ссылку на логин на страницах
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # пользователь зарегистрирован
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
