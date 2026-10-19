import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):
        self.driver.get("https://www.ebay.com/")

    def verify_home_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "gh-logo")))
        assert "eBay" in self.driver.title
        assert self.driver.find_element(By.ID, "gh-ac").is_displayed()
        assert self.driver.find_element(By.ID, "gh-search-btn").is_displayed()

    def open_category(self):
        wait = WebDriverWait(self.driver, 20)
        category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Electronics")))
        category.click()
        wait.until(EC.url_contains("/b/"))
        assert "ebay.com" in self.driver.current_url

    def search_product(self, product):
        search_box = self.driver.find_element(By.ID, "gh-ac")
        search_box.clear()
        search_box.send_keys(product)
        search_box.send_keys(Keys.ENTER)

    def verify_search_results(self, product):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.url_contains("_nkw="))
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "gh-ac")))
        actual_value = search_box.get_attribute("value")
        assert actual_value.lower() == product.lower()
        assert product.lower() in self.driver.current_url.lower()

    def take_screenshot(self, file_name):
        os.makedirs("verification", exist_ok=True)
        self.driver.save_screenshot("verification/" + file_name)
