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
    context.isbni = 'tetl'
    context.payload = add_book_payload(context.isbni)


@when('we execute the Addbook PostAPI method')
def step_impl(context):
    context.add_book_response = requests.post(context.final_url_add, json=context.payload, headers=context.head1)


@then('book is successfully added')
def step_impl(context):
    print(context.add_book_response.status_code)
    # assert context.postResponse2Json['Msg'] == "successfully added"
