from selenium import webdriver
import random

start_page_url = "http://selenium1py.pythonanywhere.com/ru/"
successful_registration_text = "Спасибо за регистрацию!"


def verify_that_user_can_register_with_correct_credentials():
    # Data
    email_seed = random.randint(2, 9999)
    test_email = f"test{email_seed}@test.kz"
    test_password = "ThisPasswordShouldBeFine"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(start_page_url)

        login_link = browser.find_element_by_css_selector('#login_link')
        login_link.click()
        email_input = browser.find_element_by_css_selector("#id_registration-email")
        password_input = browser.find_element_by_css_selector("#id_registration-password1")
        confirm_password_input = browser.find_element_by_css_selector("#id_registration-password2")
        register_button = browser.find_element_by_css_selector("[name='registration_submit']")

        email_input.clear()
        password_input.clear()
        confirm_password_input.clear()

        # Act
        email_input.send_keys(test_email)
        password_input.send_keys(test_password)
        confirm_password_input.send_keys(test_password)

        # Assert
        register_button.click()
        alert_message_displayed = browser.find_element_by_css_selector(".wicon").text
        assert successful_registration_text in alert_message_displayed, \
            "Text informing about successful registration was not displayed"

    finally:
        browser.quit()


verify_that_user_can_register_with_correct_credentials()

'''
Не смог в рамках одного .py файла вынести элементы с локаторами за рамки теста, т.к. веб-элементы не находились 
до того момента как был совершён переход на содержащую их страницу. Из доп.замечаний только вынес веб-элементы 
в отдельные переменные.
'''
