# Synchronization (Implicit & Explicit) waits in selenium
# https://rahulshettyacademy.com/seleniumPractise
# promocode: rahulshettyacademy
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from driver import CallDriver   # syntax : from fileName import ClassName


class GreenCart(CallDriver):
    def __init__(self, driver_type):
        self.type = driver_type
        CallDriver.__init__(self)

    def invoke_driver(self):
        if self.type == "headless_chrome":
            return CallDriver.call_headless_chrome(self)
        elif self.type == "chrome":
            return CallDriver.call_chrome(self)
        elif self.type == "firefox":
            return CallDriver.call_firefox(self)
        else:
            exit()


def cart_script():
    url = "https://rahulshettyacademy.com/seleniumPractise"
    browser = "headless_chrome"
    driver_obj = GreenCart(browser)
    driver = driver_obj.invoke_driver()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)
    # driver.implicitly_wait(5)
    driver.find_element_by_xpath("//input[@class='search-keyword']").send_keys('ber')
    time.sleep(4)
    # validating product count after entering ber in search box
    product_count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
    assert product_count == 3
    # clicking on all the Add to cart button
    add_to_cart = driver.find_elements_by_xpath("//div[@class='product-action']/button")
    print(len(add_to_cart))
    for button in add_to_cart:
        button.click()
        # driver.implicitly_wait(1)
    # clicking the cart icon xpath: img[alt='Cart']
    driver.find_element_by_css_selector("img[alt = 'Cart']").click()
    # driver.implicitly_wait(5)
    # clicking on proceed to checkout
    driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
    time.sleep(5)
    # explicit wait
    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
    # entering data into promo code field
    driver.find_element_by_xpath("//input[@class='promoCode']").send_keys('rahulshettyacademy')
    print(driver.current_url)
    # driver.implicitly_wait(7)
    # clicking Apply button
    driver.find_element_by_xpath("//button[@class='promoBtn']").click()
    # checking for code applied text.
    assert 'applied' in driver.find_element_by_xpath("//span[@class='promoInfo']").text

    driver.quit()


if __name__ == '__main__':
    cart_script()
