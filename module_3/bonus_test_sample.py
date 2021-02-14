from selenium import webdriver

start_page_url = "http://selenium1py.pythonanywhere.com/ru/"

login_locator = "#login_link"
alert_success_message_locator = ".wicon"

def verify_that_registered_user_can_successfully_authorize():
    # Data
    test_email = "test1@test.kz"
    test_password = "ThisPasswordShouldBeFine"

    try:
        # Assert
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.delete_all_cookies()
        browser.get(start_page_url)
        email_input_locator = "#id_login-username"
        browser.find_element_by_css_selector(email_input_locator).clear()
        password_input_locator = "#id_login-password"
        browser.find_element_by_css_selector(password_input_locator).clear()
        login_button_locator = "[name='login_submit']"
        successful_login_text = "Рады видеть вас снова"

        browser.find_element_by_css_selector(login_locator).click()

        # Act
        browser.find_element_by_css_selector(email_input_locator).send_keys(test_email)
        browser.find_element_by_css_selector(password_input_locator).send_keys(test_password)

        #Assert
        browser.find_element_by_css_selector(login_button_locator).click()
        actual_message_displayed = browser.find_element_by_css_selector(alert_success_message_locator).text

        assert successful_login_text in actual_message_displayed, \
            "Something went wrong with displaying successful login message"

    finally:
        browser.quit()

verify_that_registered_user_can_successfully_authorize()

