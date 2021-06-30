"""
Problem Statement:
Scrape the following page
https://www.zomato.com/london/best-restaurants?page=1530
And get me all the restaurant data in json format.
"""
# importing required libraries, same is also available in requirements.text file
import re
import json
import unidecode
from bs4 import BeautifulSoup
import requests


# defining a function that gets response in html format from zomato website
def get_page_html(url, page):
    custom_user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    try:
        # trying to reach url
        response = requests.get(url, headers={"User-Agent": custom_user_agent}, params={'page': page})
        if response.status_code != 200:  # checking for response status code, if not 200, throwing error
            print(response.status_code, 'Something is wrong, please check')
        else:
            # print(response.status_code)
            response_content = response.content  # when response code is 200 then storing response content.
            # print(response_soup.prettify())
            return response_content  # if response code is 200 then returning response content.
    except Error as err:
        print(err)


# defining a function that takes response content as argument, parses it as html and process further
def get_restaurants(response_content):
    # raw_html = None
    raw_html = response_content
    # parsing response content as html using  BeautifulSoup
    soup = BeautifulSoup(raw_html, 'html.parser')
    # parsing and finding required data from soup i.e. html from response content
    restaurants = []  # initializing a list of restaurants
    # selecting required data using select
    for card in soup.select('#orig-search-list > div.search-card'):
        restaurant = {}  # initializing  a restaurant as dictionary

        # searching for establishment type
        establishment_txt = None
        for establishment in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.res-snippet-small-establishment.mt5'):
            establishment_txt = establishment.get_text()
        restaurant['establishment'] = establishment_txt  # storing result values as establishment

        # searching for title of restaurant
        title_txt = None
        for title in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > a.result-title.hover_feedback.zred.bold.ln24.fontsize0'):
            title_txt = title.get_text().strip()
        restaurant['title'] = title_txt  # storing result values as restaurant title

        # searching for rating
        rating_txt = None
        for rating in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.single-rating.flex > span.rating-value'):
            rating_txt = rating.get_text()
        restaurant['rating'] = rating_txt  # storing result values as rating

        # searching for review count
        reviews_txt = None
        for reviews in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.single-rating.flex > span.review-count.medium'):
            reviews_txt = reviews.get_text().lower().replace('(', '').replace(' reviews)', '')
        restaurant['review_count'] = reviews_txt  # storing result values as review count

        # searching for locality
        locality_txt = None
        for locality in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > a.ln24.search-page-text.mr10.zblack.search_result_subzone.left'):
            locality_txt = locality.get_text()
        restaurant['locality'] = locality_txt  # storing result values as locality

        # searching for address
        address_txt = None
        for address in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(2) > div'):
            address_txt = address.get_text()
        restaurant['address'] = address_txt  # storing result values as address

        # searching for href for restaurants
        href_txt = None
        view_menu = None
        for href in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > a.result-title.hover_feedback.zred.bold.ln24.fontsize0'):
            href_txt = href.get('href')
            view_menu = href.get('href')+'/menu#tabtop'  # making view menu urls from href
        restaurant['sub_url'] = href_txt  # storing result values as sub_url

        # searching for view menu links for restaurants
        restaurant['view_menu'] = view_menu  # storing result values as view_menu

        # searching for restaurant images url
        img_url_txt = None
        for img_url in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-6.col-m-4 > div > a'):
            img_url_txt = img_url.get('data-original')
        restaurant['img_url'] = img_url_txt  # storing result values as image_url

        # searching for restaurant calling numbers
        call_txt = None
        for call in card.select('div.ui.two.item.menu.search-result-action.mt0 > a.item.res-snippet-ph-info'):
            call_txt = call.get('data-phone-no-str')
        restaurant['call'] = call_txt  # storing result values as call

        # searching for meta data like cuisines, cost for two, hours,
        for meta_tag in card.select('div.content > div > article > div.search-page-text.clearfix.row'):
            meta_tag_name_lst = list(meta_tag.select('span.ttupper'))  # storing list of meta tag names
            meta_tag_value_lst = list(meta_tag.select('.col-s-11'))  # storing list of meta tag values
            if len(meta_tag_name_lst) != len(meta_tag_value_lst):
                continue  # ignoring restaurant data that is having unequal list of meta names and value

            # meta_name_txt = None
            # meta_value_txt = None
            # storing list of meta tag names and values
            for idx in range(len(meta_tag_name_lst)):
                meta_name = meta_tag_name_lst[idx]
                meta_name_txt = meta_name.get_text()
                meta_value = meta_tag_value_lst[idx]
                meta_value_txt = meta_value.get_text().strip()
                if meta_name_txt and meta_value_txt:
                    # adding to restaurant if both meta name and value is present
                    restaurant[slugify(meta_name_txt)] = meta_value_txt

        restaurants.append(restaurant)  # appending restaurant data to restaurants list
    # pprint(restaurants)
    # print(json.dumps(restaurants, indent=2, ensure_ascii=False))
    return restaurants  # returning restaurants list from page


def slugify(text):
    # return a slugified version of passed in text
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '_', text)


# defining a main function as driver
def main():
    url = 'https://www.zomato.com/london/best-restaurants'  # declaring url to be accessed
    restaurants_list = []  # initializing a list of restaurants
    # for loop as per number of pages on url, we can change loop iteration if as pre requirement
    # range(1530, 0, -1) for all pages restaurant data
    for page in range(1530, 1529, -1):
        response_content = get_page_html(url, page)  # calling get_page_html to return response content
        # adding list of restaurants returned from get_restaurants function to restaurants_list
        restaurants_list = restaurants_list + get_restaurants(response_content)
    # pprint(restaurants_list)
    # print(len(restaurants_list))
    # dumping final restaurants_list as json
    restaurant_data = json.dumps(restaurants_list, indent=2, ensure_ascii=False)
    # writing restaurant_data json to restaurant_data.json file
    with open('./restaurant_data.json', 'w') as writer:
        writer.write(restaurant_data)
    # print(restaurant_data)


if __name__ == '__main__':
    main()
