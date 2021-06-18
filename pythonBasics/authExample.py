# Authenticating API's using Python Automation auth method- Example
# auth = ('user', 'password')
import requests
from configurations import *
from resources import *

gitAccessUrl = getconfig()['api']['gitHubUrl']
print(gitAccessUrl)
userName = getconfig()['gitHubCredentials']['userName']
# get password by user, not required as basic auth deprecated on github since 5may 2021
# def get_password():
#     password = input('Please enter GitHub password:\n')
#     return password
# session manager
with requests.Session() as sessionManager:
    HeadAccept = ApiResources.HeadAccept
    sessionManager.headers.update(HeadAccept)
    HeadAuthorize = ApiResources.HeadAuthorize
    sessionManager.headers.update(HeadAuthorize)
# requesting git hub with authorization header
# responseGitAuth = requests.get(gitAccessUrl+'/user', headers=head2)
responseGitAuth = sessionManager.get(gitAccessUrl+'/user')
print(responseGitAuth.status_code)
print(responseGitAuth.json())

# accessing octokit org's repo
pathOrgRepos = ApiResources.gitHubRepo  # preparing base url using configurations.py
repoUrl = gitAccessUrl+pathOrgRepos  # making final url by adding base url and resource path from resources.py
print(repoUrl)
responseUserRepos = sessionManager.get(repoUrl)
print(responseUserRepos.status_code)
# print(responseUserRepos.json())

