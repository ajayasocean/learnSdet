# finding and clicking radio buttons.
from driver import CallDriver   # syntax : from fileName import ClassName


class RadioButton(CallDriver):
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
    driver_obj = RadioButton(browser)
    driver = driver_obj.invoke_driver()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)
    driver.implicitly_wait(5)
    # finding radiobutton via common locator
    radio_buttons = driver.find_elements_by_name('radioButton')
    print(len(radio_buttons))
    radio_buttons[2].click()
    assert radio_buttons[2].is_selected()
    driver.quit()


if __name__ == '__main__':
    run_script()
