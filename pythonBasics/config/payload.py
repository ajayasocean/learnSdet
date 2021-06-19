# payload for add and delete post request
def add_book_payload(isbni):
    body = {
        "name": "New Day",
        "isbn": isbni,
        "aisle": "9999",
        "author": "Tester"
    }
    return body
