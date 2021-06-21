# Validating response status codes and headers using response object

import requests

baseUrl = 'http://216.10.245.166/Library/GetBook.php'
response2 = requests.get(baseUrl, params={'AuthorName': 'Tester'},)
# print('Response status code is: \t', response2)
print('Response status code is: \t', response2.status_code)  # checking status code
assert response2.status_code == 200  # asserting status code as 200
response2Header = response2.headers  # storing response headers.
print('Response headers are: \n', response2Header)  # printing response headers

# validating 'Content-Type' header is 'application/json;charset=UTF-8'
assert response2Header['Content-Type'] == 'application/json;charset=UTF-8'  # asserting for required value
if response2Header['Content-Type'] == 'application/json;charset=UTF-8':
    print('Content-Type is: \n', response2Header['Content-Type'])
else:
    print('Content-Type is not as expected')

# response cookies
print('Response cookies are: \n', response2.cookies)

# Retrieve the book details for isbn = tretrer i.e match isbn and then print complete book details.
response2Json = response2.json()
print('Search response data:\t', response2Json)
lengthOfResponse2Json = len(response2Json)
dataResponse2 = {}
for actualBook in range(lengthOfResponse2Json):  # iterating through the list
    dataResponse2 = response2Json[actualBook]  # storing element in each iteration to a variable
    if dataResponse2['isbn'] == 'tretrer':  # evaluating condition
        print(dataResponse2)  # printing resultant book details
        break
expectedBook = {
        "book_name": "ocean",
        "isbn": "tretrer",
        "aisle": "333"
    }
assert expectedBook == dataResponse2  # asserting for expected book details
