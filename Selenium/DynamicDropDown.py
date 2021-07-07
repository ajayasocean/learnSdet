# Auto-suggestive dynamic dropdowns
from driver import CallDriver   # syntax : from fileName import ClassName


class AutoDD(CallDriver):
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


def run_script():
    url = "https://rahulshettyacademy.com/AutomationPractice"
    browser = "headless_chrome"
    driver_obj = AutoDD(browser)
    driver = driver_obj.invoke_driver()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)
    driver.implicitly_wait(5)
    auto_dropdown = driver.find_element_by_id("autocomplete")
    auto_dropdown.send_keys("ind")
    driver.implicitly_wait(3)
    res_countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] div")
    print(len(res_countries))
    for country in res_countries:
        if country.text == 'India':
            print(country.text)
            country.click()
            break
    assert driver.find_element_by_id("autocomplete").get_attribute('value') == 'India'
    driver.quit()


if __name__ == '__main__':
    run_script()
