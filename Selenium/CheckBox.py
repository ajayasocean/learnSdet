# handling checkbox dynamically using selenium
from driver import CallDriver   # syntax : from fileName import ClassName


class Checkbox(CallDriver):
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
    driver_obj = Checkbox(browser)
    driver = driver_obj.invoke_driver()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)
    driver.implicitly_wait(5)
    # finding checkbox via common locator using xpath
    check_list = driver.find_elements_by_xpath("//input[@type='checkbox']")
    print(len(check_list))
    for checkbox in check_list:
        print(checkbox.get_attribute('value'))
        if checkbox.get_attribute('value') == 'Option1':
            checkbox.click()
            assert checkbox.is_selected()
    driver.quit()


if __name__ == '__main__':
    run_script()

