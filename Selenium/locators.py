from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_locators():
    # log file for chrome driver
    logger = ["--verbose", "--log-path=../selenium/chromedriver.log"]
    url1 = "https://rahulshettyacademy.com/angularpractice"

    # to run run script in chromedriver
    # driver = webdriver.Chrome(service_args=logger)

    # to run chromedriver in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service_args=logger, options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(url1)
    driver.find_element_by_id('exampleCheck1').click()  # find element by id
    driver.find_element_by_css_selector('input[name=name]').send_keys('Ajay')  # find element by css selector
    driver.find_element_by_css_selector('input[name=email]').send_keys('as')  # find element by css selector

    name_field = driver.find_element_by_name('name')  # finding element by name
    name_field.send_keys("Ajay")  # sending text to element
    # print(name_field.tag_name)
    driver.implicitly_wait(5)
    driver.quit()
    print("webdriver is done for the day")


if __name__ == '__main__':
    test_locators()
