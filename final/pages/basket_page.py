from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def get_total_on_basket_page(self):
        basket_total = self.browser.find_element(*BasketPageLocators.BASKET_TOTAL).text
        basket_value = ""
        for symbol in basket_total:
            if symbol.isdigit():
                basket_value += symbol
            elif symbol == "." or symbol == ",":
                basket_value += "."
        return float(basket_value)

    def set_product_quantity(self, quantity):
        product_quantity_input = self.browser.find_element(*BasketPageLocators.PRODUCT_QUANTITY)
        update_button = self.browser.find_element(*BasketPageLocators.UPDATE_BUTTON)
        product_quantity_input.clear()
        product_quantity_input.send_keys(str(quantity))
        update_button.click()

    def should_be_correct_basket_total(self, expected_total):
        assert self.get_total_on_basket_page() == expected_total, "Price is not correct after changing product quantity"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket should be empty but it's not!"

    def should_display_message_regarding_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Message with empty basket was not displayed"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket content is lost"
