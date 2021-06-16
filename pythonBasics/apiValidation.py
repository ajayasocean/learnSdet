# request library
# sample apis for practice on https://www.rahulshettyacademy.com/#/practice-project
# Library api contract
# https://drive.google.com/file/d/18FC3jDnsOol9zn3_KGSrjg35a4unpiSG/view
import requests
# import json
baseUrl = 'http://216.10.245.166/Library/GetBook.php'
response1 = requests.get(baseUrl, params={'AuthorName': 'Tester'},)
# print(response1.text)
# dict_response1 = json.loads(response1.text)
# print(dict_response1, '\n', type(dict_response1))
response1Json = response1.json()  # json() method process response data received from request
print(response1Json, '\n', type(response1Json))
print(response1Json[0]['isbn'])  # printing 0th element from list i.e. dictionary that too for item isbn

