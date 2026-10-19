import os
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    os.makedirs("verification",exist_ok=True)
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.set_page_load_timeout(30)
    yield browser
    browser.quit()
