from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # наличие товаров в корзине
    def products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Products in basket, but should not be"

    # тескт о наличии товаров в корзине
    def basket_text(self):
        expected_result = " "
        actual_result = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert expected_result in actual_result, "No text about empty basket"
