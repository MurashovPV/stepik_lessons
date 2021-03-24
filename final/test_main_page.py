from final.pages.main_page import MainPage
from final.pages.login_page import LoginPage
from final.pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        login_page = LoginPage(browser, browser.current_url)
        # Act
        page.open()
        page.go_to_login_page()
        # Assert
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        basket_page = BasketPage(browser, browser.current_url)
        # Act
        page.open()
        page.view_basket_page()
        # Assert
        basket_page.should_be_empty_basket()
        basket_page.should_display_message_regarding_empty_basket()


class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        # Act
        page.open()
        # Assert
        page.should_be_login_link()
