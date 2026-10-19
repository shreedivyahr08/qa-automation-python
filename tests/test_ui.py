
from pages.home_page import HomePage


# Test 1: Home page verification
def test_home_page(driver):
    page = HomePage(driver)

    page.open_home_page()
    page.verify_home_page()
    page.take_screenshot("home_page.png")


# Test 2: Category navigation
def test_category_navigation(driver):
    page = HomePage(driver)

    page.open_home_page()
    page.open_category()
    page.take_screenshot("category_page.png")


# Test 3: Product search
def test_product_search(driver):
    page = HomePage(driver)

    page.open_home_page()
    page.verify_home_page()
    page.search_product("Mobile")
    page.verify_search_results("Mobile")
    page.take_screenshot("search_results.png")
