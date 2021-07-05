from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_locators():
    # log file for chrome driver
    logger = ["--verbose", "--log-path=../selenium/chromedriver.log"]
    url1 = "https://rahulshettyacademy.com/angularpractice"
    # url2 = "https://netflix.com"
    # to run run script in chromedriver
    # driver = webdriver.Chrome(service_args=logger)
    # to run chromedriver in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service_args=logger, options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(url1)
    driver.find_element_by_name('name')
    driver.implicitly_wait(5)
    driver.quit()
    print("webdriver is done for the day")


if __name__ == '__main__':
    test_locators()
