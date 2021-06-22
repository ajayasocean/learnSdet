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
    context.isbn = 'retet'
    context.aisle = '9999'
    context.payload = add_book_payload(context.isbn, context.aisle)


@when('we execute the Addbook PostAPI method')
def step_impl(context):
    context.add_book_response = requests.post(context.final_url_add, json=context.payload, headers=context.head1)


@then('book is successfully added')
def step_impl(context):
    print(context.add_book_response.status_code, '\n')
    add_book_response_json = context.add_book_response.json()
    context.added_book_id = add_book_response_json['ID']
    print(context.added_book_id, '\n')
    print(add_book_response_json, '\n\n')
    # added /n to make sure behave doesn't overwrites our print as it used escape sequence.
    assert add_book_response_json['Msg'] == "successfully added"

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