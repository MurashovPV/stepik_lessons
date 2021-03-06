import random

add_to_basket_translations = {"en-GB": "Add to basket",
                              "ru": "Добавить в корзину",
                              "es": "Añadir al carrito",
                              "fr": "Ajouter au panier"}


def test_add_to_basket_button_should_contain_correct_value(browser, language):
    # Arrange
    catalogue_link = f"http://selenium1py.pythonanywhere.com/{language.lower()}/catalogue"
    browser.get(catalogue_link)
    goods_list = browser.find_elements_by_css_selector("h3")

    # Act
    random.choice(goods_list).click()

    # Assert
    add_to_basket_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_to_basket_button.text == add_to_basket_translations[language], "There is wrong text displayed on " \
                                                                              "'Add to Basket button'"
