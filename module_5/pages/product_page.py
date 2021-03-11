from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        for symbol in product_price:
            if symbol.isdigit():
                product_price += symbol
            elif symbol == "." or symbol == ",":
                product_price += "."
        return float(product_price)

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_added_to_basket(self):
        self.should_add_correct_product()
        self.should_update_overall_price()

    def should_add_correct_product(self):
        product_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_IN_ALERT).text
        assert product_in_alert == self.get_product_title(), "Wrong product was added into basket."

    def should_update_overall_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.BASKET_ALERT).text
        assert product_price in price_in_alert, "Wrong cost was added to basket."
