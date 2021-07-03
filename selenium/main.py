from selenium import webdriver


def chrome_driver():
    logger = ["--verbose", "--log-path=/home/ajay/drivers/chromedriver.log"]
    url1 = "https://imdb.com"
    url2 = "https://netflix.com"
    driver = webdriver.Chrome(service_args=logger)
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


if __name__ == '__main__':
    chrome_driver()

