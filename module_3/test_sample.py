from selenium import webdriver
import random

start_page_url = "http://selenium1py.pythonanywhere.com/ru/"

login_link_locator = "#login_link"
logout_lik_locator = "#logout_link"


def verify_that_user_can_register_with_correct_credentials():
    # Data
    random_number_for_generating_unique_email = random.randint(1, 9999)
    test_email = f"test{random_number_for_generating_unique_email}@test.kz"
    test_password = "ThisPasswordShouldBeFine"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(start_page_url)
        email_input_locator = "#id_registration-email"
        password_input_locator = "#id_registration-password1"
        confirm_password_input_locator = "#id_registration-password2"
        register_button_locator = "[name='registration_submit']"
        successful_registration_locator = ".wicon"
        successful_registration_text = "Спасибо за регистрацию!"

        browser.find_element_by_css_selector(login_link_locator).click()
        browser.find_element_by_css_selector(email_input_locator).clear()
        browser.find_element_by_css_selector(password_input_locator).clear()
        browser.find_element_by_css_selector(confirm_password_input_locator).clear()

        # Act
        browser.find_element_by_css_selector(email_input_locator).send_keys(test_email)
        browser.find_element_by_css_selector(password_input_locator).send_keys(test_password)
        browser.find_element_by_css_selector(confirm_password_input_locator).send_keys(test_password)

        # Assert
        browser.find_element_by_css_selector(register_button_locator).click()
        actual_message_displayed = browser.find_element_by_css_selector(successful_registration_locator).text
        assert successful_registration_text in actual_message_displayed, \
            "Text informing about successful registration was not displayed"

    finally:
        browser.quit()

