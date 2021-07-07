from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_locators():
    # log file for chrome driver
    logger = ["--verbose", "--log-path=../Selenium/chromedriver.log"]
    url1 = "https://rahulshettyacademy.com/angularpractice"
    url2 = "https://login.salesforce.com/"

    # to run run script in chromedriver
    # driver = webdriver.Chrome(service_args=logger)

    # to run chromedriver in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service_args=logger, options=chrome_options)

    # to run run script in firefox
    # driver = webdriver.Firefox()

    # the script
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(url1)
    driver.implicitly_wait(5)
    # driver.find_element_by_xpath("//input[@name='name'][@minlength='2']")  # xpath with two attributes
    # driver.find_element_by_css_selector('input[name=name]').send_keys('Ajay')  # find element by css selector
    # driver.find_element_by_css_selector('input[name=email]').send_keys('as')  # find element by css selector
    # driver.find_element_by_name('name').send_keys("Ajay")  # find element by name
    # driver.find_element_by_id('exampleCheck1').click()  # find element by id
    # driver.find_element_by_xpath("//input[@name='name'][@minlength='2']").send_keys('Ajay')
    driver.find_element_by_xpath("//input[@type='submit']").click()
    driver.implicitly_wait(2)
    # print(driver.find_element_by_class_name('alert-success').text)  # find element by class name
    # find element by css selector with regular expression, syntax: tagname[attribute*='value']
    print(driver.find_element_by_css_selector("div[class*='alert-success']").text)
    # find element by xpath with regular expression,
    # syntax1: //tagname[contains(@attribute,'value')]
    # syntax2: //*[contains(@attribute,'value')]
    message = driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text
    # assert 'fail' in message  # negative assertion
    assert 'success' in message
    driver.quit()
    print("webdriver is done for the day")


if __name__ == '__main__':
    test_locators()
