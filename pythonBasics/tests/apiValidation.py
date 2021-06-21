# request library
# sample apis for practice on https://www.rahulshettyacademy.com/#/practice-project
# Library api contract
# https://drive.google.com/file/d/18FC3jDnsOol9zn3_KGSrjg35a4unpiSG/view
import requests
# import json
baseUrl = 'http://216.10.245.166/Library/GetBook.php'
author = input('Please enter author name to search books: \n')
response1 = requests.get(baseUrl, params={'AuthorName': author},)
# print(response1.text)
# dict_response1 = json.loads(response1.text)
# print(dict_response1, '\n', type(dict_response1))
response1Json = response1.json()  # json() method process response data received from request
print('Below is the list of books:\n', response1Json)
#  print(response1Json[0]['isbn'])  # printing 0th element from list and dictionary item with keys 'isbn'
#  printing isbn key's value from response dynamically.
lengthOfResponse1Json = len(response1Json)  # finding length of list in response
print('Total number of books for the Author in response:', lengthOfResponse1Json)
searchCriteria = input('Please enter search criteria among: book_name, isbn, aisle \n')
for i in range(lengthOfResponse1Json):  # iterating through the list
    dataResponse1 = response1Json[i]  # storing element in each iteration to a variable
    print(searchCriteria, ':\t', dataResponse1[searchCriteria])  # printing as value of search criteria

# validating status code of the response received
print('Response status code is: \t', response1.status_code)
