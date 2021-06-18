# Authenticating API's using Python Automation auth method- Example
# auth = ('user', 'password')
import requests
from configurations import *
from resources import *

gitAccessUrl = getconfig()['api']['gitHubUrl']
print(gitAccessUrl)
userName = getconfig()['gitHubCredentials']['userName']
# get password by user


def get_password():
    password = input('Please enter GitHub password:\n')
    return password


# session manager
sessionManager = requests.session()
sessionManager.auth = auth = (userName, get_password())
head2 = ApiResources.acceptHeader
# requesting git hub with username and password for access
responseGitAuth = requests.get(gitAccessUrl+'/user', headers=head2, auth=(userName, get_password()))
# responseGitAuth = sessionManager.get(gitAccessUrl+'/user', headers=head2)
print(responseGitAuth.status_code)
# print(responseGitAuth.text)

# accessing an org repo
pathOrgRepos = ApiResources.gitHubRepo  # preparing base url using configurations.py
repoUrl = gitAccessUrl+pathOrgRepos  # making final url by adding base url and resource path from resources.py
print(repoUrl)
responseUserRepos = requests.get(repoUrl, headers=head2)
print(responseUserRepos.status_code)
# print(responseUserRepos.json())

