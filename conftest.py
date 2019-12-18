import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="en",
					 help="Choose language: ru, en, es, fr, ...")
	parser.addoption('--browser_name', action='store', default="chrome",
					 help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")
	browser_name = request.config.getoption("browser_name")

	if browser_name == "chrome":
		options = Options()
		options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		print(f"\nstart chrome browser with {user_language} language")
		#browser = webdriver.Chrome(options=options)
		browser = webdriver.Chrome(options=options, executable_path="C:/chromedriver/chromedriver.exe", )  
	elif browser_name == "firefox":
		print("\nstart firefox browser for test..")
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		browser = webdriver.Firefox(firefox_profile=fp)
	else:
		raise pytest.UsageError("--browser_name should be chrome or firefox")
	yield browser
	browser.quit()
