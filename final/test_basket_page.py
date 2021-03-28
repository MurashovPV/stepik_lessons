from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.catalogue_page import CataloguePage
from .pages.login_page import LoginPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"


class TestBasketPage:
    @pytest.mark.personal_tests
    def test_basket_is_not_lost_after_login(self, browser):
        # Arrange
        page = MainPage(browser, link)
        catalogue_page = CataloguePage(browser, browser.current_url)
        login_page = LoginPage(browser, browser.current_url)
        basket_page = BasketPage(browser, browser.current_url)
        # Act
        page.open()
        page.navigate_to_catalogue()
        catalogue_page.add_to_basket_any_product()
        page.go_to_login_page()
        login_page.register_new_user("new@test.kz", "ThisPasswordIsOK")
        page.view_basket_page()
        # Assert
        basket_page.should_not_be_empty_basket()

    @pytest.mark.personal_tests
    def test_basket_total_updates_after_changing_product_quantity(self, browser):
        # Arrange
        page = MainPage(browser, link)
        catalogue_page = CataloguePage(browser, browser.current_url)
        basket_page = BasketPage(browser, browser.current_url)
        # Act
        page.open()
        page.navigate_to_catalogue()
        catalogue_page.add_to_basket_any_product()
        page.view_basket_page()
        basket_page.set_product_quantity(1)
        previous_total = basket_page.get_total_on_basket_page()
        basket_page.set_product_quantity(2)
        # Assert
        basket_page.should_be_correct_basket_total(previous_total * 2)
