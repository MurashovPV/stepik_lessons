from final.pages.login_page import LoginPage
from final.pages.main_page import MainPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"


class TestLoginPage:
    @pytest.mark.personal_tests
    def test_guest_can_login(self, browser):
        page = MainPage(browser, link)
        login_page = LoginPage(browser, browser.current_url)
        page.open()
        page.go_to_login_page()
        login_page.log_in("existent@user.kz", "ThisPasswordShouldBeOk")
        page.should_be_authorized_user()

    @pytest.mark.personal_tests
    @pytest.mark.parametrize("email", ["dotsindomain@a.s.a.p", "invalid@domain"])
    def test_guest_cant_register_with_invalid_email(self, browser, email):
        # Arrange
        page = MainPage(browser, link)
        login_page = LoginPage(browser, browser.current_url)
        # Act
        page.open()
        page.go_to_login_page()
        login_page.register_new_user(email, "ThisPasswordShouldBeOk")
        # Assert
        login_page.should_be_invalid_email()

    @pytest.mark.personal_tests
    def test_guest_cant_register_with_existent_email(self, browser):
        # Arrange
        page = MainPage(browser, link)
        login_page = LoginPage(browser, browser.current_url)
        # Act
        page.open()
        page.go_to_login_page()
        login_page.try_to_register_existent_user("existent@user.kz", "ThisPasswordShouldBeOk")
        # Assert
        login_page.should_be_invalid_email()
