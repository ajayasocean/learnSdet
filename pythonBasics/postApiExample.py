# Understand automating Post http request with Payload and headers
import requests
import json
# Add a new book
with open ('/home/ajay/learnSdet/pythonBasics/postRequestDataJsonFile.json', 'r') as j:
    requestDataJson = json.load(j)
baseUrl = 'http://216.10.245.166/Library/Addbook.php'
head1 = {'Content-Type': 'application/json'}
postResponse1 = requests.post(baseUrl, json=requestDataJson, headers=head1,)
assert postResponse1.status_code == 200
postResponse1Json = postResponse1.json()
print(postResponse1Json)
print(type(postResponse1Json))

