# payload for add and book post request
from config.configurations import *


def add_book_payload(isbni):
    body = {
        "name": "New Day",
        "isbn": isbni,
        "aisle": "9999",
        "author": "Tester"
    }
    return body


# building post data (body) for add book request using get_query function.
def build_payload_from_db(add_book_query):
    make_body = {}
    result_set_data = get_query(add_book_query)
    make_body['name'] = result_set_data[0]
    make_body['isbn'] = result_set_data[1]
    make_body['aisle'] = result_set_data[2]
    make_body['author'] = result_set_data[3]
    return make_body
