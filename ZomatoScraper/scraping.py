import re
import json
import unidecode
from bs4 import BeautifulSoup
import requests


def get_page_html(url, page):
    custom_user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    response = requests.get(url, headers={"User-Agent": custom_user_agent}, params={'page': page})
    if response.status_code == 200:
        # print(response.status_code, 'ok, Lets begin...')
        response_html = response.content
        # print(response_soup.prettify())
        return response_html
    else:
        print("unable to access", url)


def get_restaurants(response_html):
    raw_html = None
    raw_html = response_html
    soup = BeautifulSoup(raw_html, 'html.parser')
    restaurants = []

    for card in soup.select('#orig-search-list > div.search-card'):
        restaurant = {}

        establishment_txt = None
        for establishment in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.res-snippet-small-establishment.mt5'):
            establishment_txt = establishment.get_text()
        restaurant['establishment'] = establishment_txt

        title_txt = None
        for title in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > a.result-title.hover_feedback.zred.bold.ln24.fontsize0'):
            title_txt = title.get_text().strip()
        restaurant['title'] = title_txt

        rating_txt = None
        for rating in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.single-rating.flex > span.rating-value'):
            rating_txt = rating.get_text()
        restaurant['rating'] = rating_txt

        reviews_txt = None
        for reviews in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > div.single-rating.flex > span.review-count.medium'):
            reviews_txt = reviews.get_text().lower().replace('(', '').replace(' reviews)', '')
        restaurant['review_count'] = reviews_txt

        locality_txt = None
        for locality in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > a.ln24.search-page-text.mr10.zblack.search_result_subzone.left'):
            locality_txt = locality.get_text()
        restaurant['locality'] = locality_txt

        address_txt = None
        for address in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(2) > div'):
            address_txt = address.get_text()
        restaurant['address'] = address_txt

        href_txt = None
        for href in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-16.col-m-12.pl0 > div:nth-child(1) > div.col-s-12 > a.result-title.hover_feedback.zred.bold.ln24.fontsize0'):
            href_txt = href.get('href')
        restaurant['sub_url'] = href_txt

        img_url_txt = None
        for img_url in card.select(
                'div.content > div > article > div.pos-relative.clearfix > div > div.col-s-6.col-m-4 > div > a'):
            img_url_txt = img_url.get('data-original')
        restaurant['img_url'] = img_url_txt

        call_txt = None
        for call in card.select('div.ui.two.item.menu.search-result-action.mt0 > a.item.res-snippet-ph-info'):
            call_txt = call.get('data-phone-no-str')
        restaurant['call'] = call_txt

        meta_tag_lst = list(card.select('div.content > div > article > div.search-page-text.clearfix.row'))

        for meta_tag in meta_tag_lst:

            meta_tag_name_lst = list(meta_tag.select('span.ttupper'))
            meta_tag_value_lst = list(meta_tag.select('.col-s-11'))
            if len(meta_tag_name_lst) != len(meta_tag_value_lst):
                continue

            meta_name_txt = None
            meta_value_txt = None
            for idx in range(len(meta_tag_name_lst)):
                meta_name = meta_tag_name_lst[idx]
                meta_name_txt = meta_name.get_text()
                meta_tag = meta_tag_value_lst[idx]
                meta_value_txt = meta_tag.get_text().strip()
                if meta_name_txt and meta_value_txt:
                    restaurant[slugify(meta_name_txt)] = meta_value_txt

        restaurants.append(restaurant)
    # pprint(restaurants)
    # print(json.dumps(restaurants, indent=2, ensure_ascii=False))
    return restaurants


def slugify(text):
    # return a slugified version of passed in text
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '_', text)


def main():
    url = 'https://www.zomato.com/london/best-restaurants'
    restaurants_list = []
    for page in range(1530, 1529, -1):
        response_html = get_page_html(url, page)
        restaurants_list = restaurants_list + get_restaurants(response_html)
    # pprint(restaurants_list)
    # print(len(restaurants_list))
    restaurant_data = json.dumps(restaurants_list, indent=2, ensure_ascii=False)
    with open('./restaurant_data.json', 'w') as writer:  # writing output to json file
        writer.write(restaurant_data)
    print(restaurant_data)


if __name__ == '__main__':
    main()
