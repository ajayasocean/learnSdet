from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def web_driver():
    # log file for chrome driver
    logger = ["--verbose", "--log-path=../Selenium/chromedriver.log"]
    url1 = "https://imdb.com"
    url2 = "https://netflix.com"

    # to run run script in chromedriver
    # driver = webdriver.Chrome(service_args=logger)

    # to run chromedriver in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service_args=logger, options=chrome_options)

    # to run run script in firefox
    # driver = webdriver.Firefox()

    # to run gekodriver in headless mode, facing a bug
    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument("--headless")
    # driver = webdriver.Firefox(options=firefox_options)

    # the script
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(url1)
    driver.implicitly_wait(10)
    print(driver.title)
    print(driver.current_url)
    driver.get(url2)  # navigating to new url
    driver.implicitly_wait(10)
    driver.back()
    driver.implicitly_wait(10)
    driver.refresh()
    driver.minimize_window()
    driver.implicitly_wait(5)
    driver.quit()
    print("webdriver is done for the day")


if __name__ == '__main__':
    web_driver()
