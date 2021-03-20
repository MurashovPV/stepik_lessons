import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
                              "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        page = ProductPage(browser, f"{link}?promo={promo_offer}")
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_added_to_basket()

    @pytest.mark.xfail(reason="this bug is never going to be fixed")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="this bug is never going to be fixed")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_disappear_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.view_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_display_message_regarding_empty_basket()


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user("super@test.kz", "ThisPasswordShouldBeFine")
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_added_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
