from pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_number', ["0", "1", "2", "3", "4", "5", "6",							
								  pytest.param("7", marks=pytest.mark.xfail),
								  "8", "9"])

def test_guest_can_add_product_to_basket(browser, promo_number):
	link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.should_appear_message_about_added_product_with_correct_product_name()
	page.should_appear_message_about_basket_total_with_correct_value()
