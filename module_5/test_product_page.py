import pytest
from .pages.product_page import ProductPage

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
