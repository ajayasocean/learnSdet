# program to write an api request to set cookie in users machine.
import requests
from config.configurations import *
from config.resources import *
# accessing url from configurations.py in-turn from globalProperties.ini
http_bin_url = get_config()['api']['http_bin']
# accessing path from resources.py
http_bin_cookies_path = ApiResources.http_bin_cookies
# making final url
final_cookie_url = http_bin_url + http_bin_cookies_path
print(final_cookie_url)
# opening session manager with headers
with requests.Session() as session_manager:
    # setting header as accept
    head_accept = ApiResources.head_accept
    session_manager.headers.update(head_accept)
    # setting cookies as cookie from resources.py
    cookie = ApiResources.cookie
    session_manager.cookies.update(cookie)
    # this cookie is for this program implicitly
    cookie_year = {'visit_year': '2021'}
    # hitting final url with cookies argument
    cookie_response = session_manager.get(final_cookie_url, cookies=cookie_year, timeout=1)
    # printing response
    # print(cookie_response.history)
    print(cookie_response.status_code)
    print(cookie_response.text)
# checking for request history
# accessing url
rahul_url = get_config()['api']['rahul_url']
print(rahul_url)
# sending request
hist_response = requests.get(rahul_url, allow_redirects=True, timeout=1)
print(hist_response.history)
print(hist_response.status_code)
# allow_redirects = False
redirect_response = requests.get(rahul_url, allow_redirects=False, timeout=1)
print(redirect_response.history)
print(redirect_response.status_code)

# sending attachment in a api request (POST)
# https://petstore.swagger.io/v2/pet/{petId}/uploadImage
# accessing base url from configurations.py in-turn from globalProperties.ini
pet_store_url = get_config()['api']['pet_store_url']
# accessing path from resources.py
pet_store_pet = ApiResources.pet_store_pet
# asking user to enter petId as it will be used as a path parameter
petId = input('Please enter valid petID\n')  # enter 9843217
petId_resource = '/'+petId
pet_store_upload = ApiResources.pet_store_upload
finalUrl = pet_store_url+pet_store_pet+petId_resource+pet_store_upload
print(finalUrl)
# accessing a sample File
file = {'file': open('/home/ajay/upload_file_sample.png', 'rb')}
upload_response = requests.post(finalUrl, files=file)
print(upload_response.status_code)
print(upload_response.text)
