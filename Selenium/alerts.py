# Handling Java/JavaScript Alert pop-ups using selenium

from driver import CallDriver   # syntax : from fileName import ClassName


class AlertPopup(CallDriver):
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


def alert_script():
    url = "https://rahulshettyacademy.com/AutomationPractice"
    browser = "headless_chrome"
    driver_obj = AlertPopup(browser)
    driver = driver_obj.invoke_driver()
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.title)
    driver.implicitly_wait(5)
    # single option alert
    driver.find_element_by_xpath("//input[@name='enter-name']").send_keys('Test')
    driver.find_element_by_id('alertbtn').click()
    # DeprecationWarning: use driver.switch_to.alert instead alert = driver.switch_to_alert()
    alert = driver.switch_to.alert
    print(alert.text)
    assert 'Test' in alert.text
    # accepting the alert to close it
    alert.accept()
    # 2 option alert (cancelling an alert)
    driver.find_element_by_xpath("//input[@name='enter-name']").send_keys('Test')
    driver.find_element_by_id('confirmbtn').click()
    # DeprecationWarning: use driver.switch_to.alert instead alert = driver.switch_to_alert()
    alert_bi = driver.switch_to.alert
    print(alert_bi.text)
    # cancelling the alert to close it
    alert.dismiss()
    driver.quit()


if __name__ == '__main__':
    alert_script()
