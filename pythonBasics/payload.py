# payload for add and delete post request
def addBookPayload(isbnIn):
    body = {
        "name": "New Day",
        "isbn": isbnIn,
        "aisle": "9999",
        "author": "Tester"
    }
    return body
