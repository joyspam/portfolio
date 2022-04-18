from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):

        self.browser.find_element(*LoginPageLocators.LOGIN).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password)
        reg_user = self.browser.find_element(*LoginPageLocators.REG_USER)
        reg_user.click()
        assert self.is_element_present(*LoginPageLocators.REG_OK), "Registration is failed"

    # login есть в текущем url, есть формы логина и регистрации
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "'login' is not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" 

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
        
