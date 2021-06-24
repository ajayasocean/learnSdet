# step implementation for the features written in BookApi.feature
# if we dont define steps from features written in feature file and run the feature file via
# >> cd /home/ajay/learnSdet/pythonBasics/features/ >> behave
# this run will provide us with steps definition syntax in terminal
from behave import *
import requests
from config.resources import *
from config.payload import *

# Add book api function


@given('the book details which needs to be added to library')
def step_impl(context):
    base_url = get_config()['api']['endpoint']
    print(base_url)
    path_add = ApiResources.addBook
    context.final_url_add = base_url + path_add
    context.head1 = {'Content-Type': 'application/json'}
    context.isbn = 'rtyrtt'
    context.aisle = '9999'
    context.payload = add_book_payload(context.isbn, context.aisle)


@when('we execute the Addbook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.final_url_add, json=context.payload, headers=context.head1)


@then('book is successfully added')
def step_impl(context):
    print(context.response.status_code, '\n')
    context.add_book_response_json = context.response.json()
    context.added_book_id = context.add_book_response_json['ID']
    print(context.added_book_id, '\n')
    print(context.add_book_response_json, '\n\n')
    # added /n to make sure behave doesn't overwrites our print as it used escape sequence.
    assert context.add_book_response_json['Msg'] == "successfully added"


@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    base_url = get_config()['api']['endpoint']
    print(base_url)
    path_add = ApiResources.addBook
    context.final_url_add = base_url + path_add
    context.head1 = {'Content-Type': 'application/json'}
    context.isbn = isbn
    context.aisle = aisle
    context.payload = add_book_payload(context.isbn, context.aisle)


@given('I have github access token')
def step_impl(context):
    context.gitAccessUrl = get_config()['api']['gitHubUrl']
    print(context.gitAccessUrl)
    # userName = get_config()['gitHubCredentials']['userName']
    # get password by user, not required as basic auth deprecated on github since 5may 2021
    # session manager
    with requests.Session() as context.sessionManager:
        head_accept = ApiResources.HeadAccept
        context.sessionManager.headers.update(head_accept)
        token = input('Please enter GitHub access token:\n')
        resource_obj = ApiResources(token)
        head_authorize = resource_obj.get_auth_token()
        context.sessionManager.headers.update(head_authorize)


@when('I hit github user resource')
def step_impl(context):
    # requesting git hub with authorization header
    context.response = context.sessionManager.get(context.gitAccessUrl + '/user')


@then('status code of response should be {status_code:d}')  # :d as input value is integer
def step_impl(context, status_code):
    print(context.response.status_code, '\n')
    assert context.response.status_code == status_code
    # print(context.response_git_auth.json())
