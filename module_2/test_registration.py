from selenium import webdriver
from sys import argv

script_name, link = argv

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_text = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    first_name_text.send_keys("Pavel")

    last_name_text = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    last_name_text.send_keys("Murashov")

    email_text = browser.find_element_by_css_selector(".third")
    email_text.send_keys("johhny@test.kz")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    browser.quit()
