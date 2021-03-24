from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "id_login-password")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "//*[@id=\"login_form\"]/p/a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".add-to-basket")
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, ".btn-wishlist")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRODUCT_ADDED_IN_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    OFFER_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(2)")
    BASKET_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(3)")
