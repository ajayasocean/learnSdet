# managing dropdowns on webpage
from selenium.webdriver.support.select import Select

from driver import CallDriver   # syntax : from fileName import ClassName


class DdPage(CallDriver):
    def __init__(self, driver_type):
        self.type = driver_type
        CallDriver.__init__(self)

    def initiate_driver(self):
        if self.type == "headless_chrome":
            return CallDriver.call_headless_chrome(self)
        elif self.type == "chrome":
            return CallDriver.call_chrome(self)
        elif self.type == "firefox":
            return CallDriver.call_firefox(self)
        else:
            exit()


def run_script():
    url = "https://rahulshettyacademy.com/angularpractice"
    browser = "firefox"
    driver_obj = DdPage(browser)
    driver = driver_obj.initiate_driver()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)
    driver.implicitly_wait(5)
    dropdown1 = Select(driver.find_element_by_id("exampleFormControlSelect1"))
    driver.implicitly_wait(5)
    print(dropdown1.select_by_visible_text("Female"))
    driver.implicitly_wait(5)
    print(dropdown1.select_by_index(0))
    driver.implicitly_wait(5)
    # print(dropdown1.select_by_value("value of element"))
    driver.quit()


if __name__ == '__main__':
    run_script()
