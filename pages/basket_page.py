from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.ADDED_PRODUCTS), "There is products in your basket, but it should be empty"

	def should_has_disclaimer_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_DISCLAIMER), "There is no YOUR BASKET IS EMPTY disclaimer on the empty basket page"

		