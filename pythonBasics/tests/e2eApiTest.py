# End to end automation flow of API calls using Python
import requests
from config.resources import *
from config.payload import *
baseUrl = get_config()['api']['endpoint']
print(baseUrl)
# Add a new book
pathAdd = ApiResources.addBook
finalUrlAdd = baseUrl+pathAdd
head1 = {'Content-Type': 'application/json'}
# using adding book fuction via a data file and not mysql
isbni = 'temper'
postResponse2 = requests.post(finalUrlAdd, json=add_book_payload(isbni), headers=head1,)
# calling in get_query function, sending add_book_query (actual sql query) as argument
add_book_query = 'select * from Books'
# postResponse2 = requests.post(finalUrlAdd, json=build_payload_from_db(add_book_query), headers=head1,)
print(postResponse2.status_code)
postResponse2Json = postResponse2.json()
print('Book successfully added', postResponse2Json)
print(type(postResponse2Json))

# Deleting the added book
pathDel = ApiResources.delBook
finalUrlDel = baseUrl+pathDel
addedBookId = postResponse2Json['ID']
print(addedBookId)
deleteResponse = requests.post(finalUrlDel, json={'ID': addedBookId}, headers=head1,)
assert deleteResponse.status_code == 200
deleteResponseJson = deleteResponse.json()
print(deleteResponseJson)
assert deleteResponseJson['msg'] == 'book is successfully deleted'
