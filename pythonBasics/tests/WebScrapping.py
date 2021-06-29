"""
Web Scrapping using BeautifulSoup and requests package.
"""
import requests
import json
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm'
if requests.get(url).status_code == 200:
    custom_User_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    # payload = {'format': 'ajax'}
    response = requests.get(url, headers={"User-Agent": custom_User_agent})
    html_text = response.text
    print(html_text)
    # response_soup = BeautifulSoup(response.content, 'html.parser')
    # # print(response_soup.prettify())
    # result_table = response_soup.find('table', {'class': 'findList'})
    # # print(result_table.text)
    # table_rows = result_table.find_all_next('tr')
    # print(table_rows)

else:
    print("Unable to retieve data, please check for issues")