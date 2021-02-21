from selenium import webdriver

start_page_url = "http://selenium1py.pythonanywhere.com/ru/"

alert_success_message_locator = ".wicon"
successful_login_text = "Рады видеть вас снова"


def verify_that_registered_user_can_successfully_authorize():
    # Data
    test_email = "test1@test.kz"
    test_password = "ThisPasswordShouldBeFine"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.delete_all_cookies()
        browser.get(start_page_url)

        login_link = browser.find_element_by_css_selector("#login_link")
        login_link.click()

        email_input = browser.find_element_by_css_selector("#id_login-username")
        password_input = browser.find_element_by_css_selector("#id_login-password")
        login_button = browser.find_element_by_css_selector("[name='login_submit']")

        email_input.clear()
        password_input.clear()

        # Act
        email_input.send_keys(test_email)
        password_input.send_keys(test_password)

        # Assert
        login_button.click()
        actual_message_displayed = browser.find_element_by_css_selector(alert_success_message_locator).text
        assert successful_login_text in actual_message_displayed, \
            "Something went wrong with displaying successful login message"

    finally:
        browser.quit()


verify_that_registered_user_can_successfully_authorize()
