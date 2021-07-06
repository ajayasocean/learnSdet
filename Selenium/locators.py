from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_locators():
    # log file for chrome driver
    logger = ["--verbose", "--log-path=../Selenium/chromedriver.log"]
    url1 = "https://rahulshettyacademy.com/angularpractice"

    # to run run script in chromedriver
    # driver = webdriver.Chrome(service_args=logger)

    # to run chromedriver in headless mode
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(service_args=logger, options=chrome_options)

    # to run run script in firefox
    driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(url1)
    driver.implicitly_wait(5)
    # driver.find_element_by_xpath("//input[@name='name'][@minlength='2']")  # xpath with two attributes
    # driver.find_element_by_css_selector('input[name=name]').send_keys('Ajay')  # find element by css selector
    # driver.find_element_by_css_selector('input[name=email]').send_keys('as')  # find element by css selector
    # driver.find_element_by_name('name').send_keys("Ajay")  # find element by name
    driver.find_element_by_id('exampleCheck1').click()  # find element by id
    driver.find_element_by_xpath("//input[@name='name'][@minlength='2']").send_keys('Ajay')
    driver.find_element_by_xpath("//input[@type='submit']").click()
    driver.implicitly_wait(5)
    print(driver.find_element_by_class_name('alert-success').text)  # find element by class name
    # driver.quit()
    print("webdriver is done for the day")


if __name__ == '__main__':
    test_locators()
