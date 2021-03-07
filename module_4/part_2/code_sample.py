from selenium import webdriver
import random
import pytest

start_page_url = "http://selenium1py.pythonanywhere.com/ru/"
successful_registration_text = "Спасибо за регистрацию!"


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


def test_user_can_register_with_correct_credentials(browser):
    # Data
    email_seed = random.randint(3, 9999)
    test_email = f"test{email_seed}@test.ru"
    test_password = "ThisPasswordShouldBeFine"

    # Arrange
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
        "Successful registration text was not displayed"
