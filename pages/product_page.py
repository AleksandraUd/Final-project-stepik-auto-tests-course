from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
	def add_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		button.click()
		self.solve_quiz_and_get_code()

	def should_appear_message_about_added_product_with_correct_product_name(self):
		self.should_appear_message_about_added_product()
		self.should_name_of_added_product_be_correct()
		
	def should_appear_message_about_added_product(self):
		assert self.is_element_present(*ProductPageLocators.FIRST_ALERT), "There is no message about adding product to the card"

	def should_name_of_added_product_be_correct(self):
		assert self.is_element_present(*ProductPageLocators.FIRST_ALERT_PRODUCT_NAME), "The name of the added product is not present in the message about adding product to the card"
		assert self.read_innerHTML(*ProductPageLocators.FIRST_ALERT_PRODUCT_NAME)==self.read_innerHTML(*ProductPageLocators.PRODUCT_NAME), "The name of the added product is incorrect"

	def should_appear_message_about_basket_total_with_correct_value(self):
		self.should_appear_message_about_basket_total()
		self.should_be_equal_with_product_price()

	def should_appear_message_about_basket_total(self):
		assert self.is_element_present(*ProductPageLocators.THIRD_ALERT), "There is no message about your card total"

	def should_be_equal_with_product_price(self):
		assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "The value of your card total is not present in the message about your card total"
		assert self.read_innerHTML(*ProductPageLocators.BASKET_TOTAL)==self.read_innerHTML(*ProductPageLocators.PRODUCT_PRICE), "Your card total is not equal to the product price"

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



