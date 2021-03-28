from .base_page import BasePage
from .locators import LoginPageLocators
import time

login_url = "/accounts/login/"
link = "http://selenium1py.pythonanywhere.com/"


class LoginPage(BasePage):
    def log_in(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).clear()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).clear()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).clear()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(str(time.time()) + email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not displayed"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.endswith(login_url), "Login url is not correct"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not displayed"

    def should_be_registration_generic_alert(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_GENERIC_ALERT), "Generic alert in registration form " \
                                                            "is not displayed"

    def should_be_registration_invalid_email_alert(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_ALERT), "Invalid email error message is " \
                                                                                     "not displayed"

    def should_be_invalid_email(self):
        self.should_be_registration_generic_alert()
        self.should_be_registration_invalid_email_alert()

    def try_to_register_existent_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).clear()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).clear()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).clear()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
