from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	ADDED_PRODUCTS = (By.CSS_SELECTOR, ".basket-items")
	EMPTY_BASKET_DISCLAIMER = (By.CSS_SELECTOR, "#content_inner>p")


#class MainPageLocators():


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
	EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
	REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	FIRST_ALERT = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner")
	FIRST_ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner strong")
	SECOND_ALERT = (By.CSS_SELECTOR, "#messages .alert:nth-child(2) .alertinner")
	THIRD_ALERT = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner p")
	BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner p strong")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

