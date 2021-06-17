# End to end automation flow of API calls using Python
import requests
from configurations import *
from resources import *
from payload import *
baseUrl = getconfig()['api']['endpoint']
print(baseUrl)
# Add a new book
pathAdd = ApiResources.addBook
finalUrlAdd = baseUrl+pathAdd
head1 = {'Content-Type': 'application/json'}
postResponse2 = requests.post(finalUrlAdd, json=addBookPayload('mill'), headers=head1,)
assert postResponse2.status_code == 200
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
