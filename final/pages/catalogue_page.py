from .base_page import BasePage
from .locators import CataloguePageLocators
import random


class CataloguePage(BasePage):
    def add_to_basket_any_product(self):
        products = self.browser.find_elements(*CataloguePageLocators.ADD_TO_BASKET_BUTTON)
        any_product = random.choice(products)
        any_product.click()

    def should_display_products(self):
        assert self.is_element_present(*CataloguePageLocators.PRODUCTS_LIST), "List with products is not displayed"

    def navigate_to_next_page(self):
        next_page_link = self.browser.find_element(*CataloguePageLocators.NEXT_PAGE_LINK)
        next_page_link.click()

    def navigate_to_any_product(self):
        products = self.browser.find_elements(*CataloguePageLocators.PRODUCT_TITLE)
        any_product = random.choice(products)
        any_product.click()
