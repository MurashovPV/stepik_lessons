from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_basket_total(self):
        product_price = ""
        basket_total = self.browser.find_element(*BasePageLocators.BASKET_TOTAL).text
        for symbol in basket_total:
            if symbol.isdigit():
                product_price += symbol
            elif symbol == "." or symbol == ",":
                product_price += "."
        return float(product_price)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def logout(self):
        logout_link = self.browser.find_element(*BasePageLocators.LOGOUT_LINK)
        logout_link.click()

    def navigate_to_main_page(self):
        main_page_link = self.browser.find_element(*BasePageLocators.OSCAR_LINK)
        main_page_link.click()

    def open(self):
        self.browser.get(self.url)

    def search_product(self, product):
        search_input = self.browser.find_element(*BasePageLocators.SEARCH_INPUT)
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        search_input.send_keys(product)
        search_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_logged_out(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not displayed after logout attempt"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def view_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        basket_link.click()
