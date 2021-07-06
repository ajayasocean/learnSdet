from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def more_locators():
    # log file for chrome driver
    logger = ["--verbose", "--log-path=../Selenium/chromedriver.log"]
    url = "https://login.salesforce.com/"

    # to run run script in chromedriver
    # driver = webdriver.Chrome(service_args=logger)

    # to run chromedriver in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service_args=logger, options=chrome_options)

    # to run run script in firefox
    # driver = webdriver.Firefox()

    # the script
    # further into locators, lets use a different website.
    driver.get(url)
    driver.implicitly_wait(5)

    # generate css from ID
    driver.find_element_by_css_selector("input#username").send_keys('test')

    # generate css from className
    driver.find_element_by_css_selector("input.password").send_keys('test')

    # element.clear()
    driver.find_element_by_css_selector("input.password").clear()

    # find element by linktext
    driver.find_element_by_link_text("Forgot Your Password?").click()
    driver.quit()
    print("webdriver is done for the day")


if __name__ == '__main__':
    more_locators()
