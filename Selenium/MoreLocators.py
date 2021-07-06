from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def more_locators():
    # log file for chrome driver
    logger = ["--verbose", "--log-path=../Selenium/chromedriver.log"]
    url = "https://login.salesforce.com"

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

    # generate css from ID : Syntax: tagname#id
    driver.find_element_by_css_selector("input#username").send_keys('test')

    # generate css from className: syntax: tagname.class_name
    driver.find_element_by_css_selector("input.password").send_keys('test')

    # element.clear() :
    driver.find_element_by_css_selector("input.password").clear()

    # find element by linktext
    driver.find_element_by_link_text("Forgot Your Password?").click()
    driver.implicitly_wait(5)
    print(driver.current_url)

    # find element by text based xpath: syntax: //tagname[text()='text_of_element']
    driver.find_element_by_xpath("//a[text()='Need Help Logging In?']")
    driver.implicitly_wait(5)
    print(driver.current_url)
    driver.back()
    driver.back()
    driver.implicitly_wait(5)
    print(driver.current_url)

    # find element using xpath by traversing tags, syntax: //tagname[@attribute='value']/childtag
    if driver.find_element_by_xpath("//div[@id='usernamegroup']/label").is_displayed():
        print('Yes')

    # find element using css by traversing tags, syntax: tagname[attribute= 'value'] childtag
    if driver.find_element_by_css_selector("form[id='login_form'] label").is_displayed():
        print('Yes')

    # find element using xpath traversing grand parent tags,
    # syntax: //grandparent_tagname[@attribute=value]/div[n]/label
    if driver.find_element_by_xpath("//form[@name='login']/div[1]/label").is_displayed():
        print('Yes')

    # find element using xpath traversing grand parent tags,
    # syntax: tagname[atrribute='value'] label:nth-child(1)
    if driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").is_displayed():
        print('Yes')

    driver.quit()
    print("webdriver is done for the day")


if __name__ == '__main__':
    more_locators()
