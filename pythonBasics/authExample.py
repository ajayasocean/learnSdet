# Authenticating API's using Python Automation auth method- Example
# auth = ('user', 'password')
from configurations import *
import requests

url = getconfig()['api']['gitHubUrl']
userName = getconfig()['gitHubCredentials']['userName']


def getPassword():
    password = input('Please enter GitHub password:\n')
    return password


responseGit = requests.get(url, auth=(userName, getPassword()))
print(responseGit.status_code)