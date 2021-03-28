import pytest
from .pages.catalogue_page import CataloguePage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/"


class TestCataloguePage:
    @pytest.mark.personal_tests
    def test_catalogue_displays_products(self, browser):
        # Arrange
        page = CataloguePage(browser, link)
        # Act
        page.open()
        page.navigate_to_next_page()
        # Assert
        page.should_display_products()

    @pytest.mark.personal_tests
    @pytest.mark.parametrize("search_string", ["agile", "pussyfoot", "testers", "hacking"])
    def test_guest_can_use_search_input(self, browser, search_string):
        # Arrange
        page = CataloguePage(browser, link)
        product_page = ProductPage(browser, browser.current_url)
        # Act
        page.open()
        page.search_product(search_string)
        page.navigate_to_any_product()
        # Assert
        product_page.should_contain_search_string(search_string)
