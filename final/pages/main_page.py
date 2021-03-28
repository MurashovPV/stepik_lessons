from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def navigate_to_catalogue(self):
        catalogue_link = self.browser.find_element(*MainPageLocators.CATALOGUE_LINK)
        catalogue_link.click()
