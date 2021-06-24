# this file may contain after scenario, before scenario
import requests

from config.resources import ApiResources
from config.payload import *


def after_scenario(context, scenario):
    if 'library' in scenario.tags:

        # Deleting the added book
        base_url = get_config()['api']['endpoint']
        path_del = ApiResources.delBook
        final_url_del = base_url + path_del
        # print(final_url_del, '\n')
        head1 = {'Content-Type': 'application/json'}
        context.response = requests.post(final_url_del, json={'ID': context.added_book_id}, headers=head1, )
        assert context.response.status_code == 200
        delete_response = context.response.json()
        print(delete_response, '\n')
        assert delete_response['msg'] == 'book is successfully deleted'
    else:
        print('skipped due to no or different tag')
