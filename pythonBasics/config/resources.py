# defining api resources
class ApiResources:
    addBook = '/Library/Addbook.php'
    delBook = '/Library/DeleteBook.php'
    getBookByAuthorName = '/Library/GetBook.php'
    gitHubRepo = '/orgs/octokit/repos'
    HeadAccept = {'Accept': 'application/vnd.github.v3+json'}
    head_accept = {'Accept': 'application/json'}
    http_bin_cookies = '/cookies'
    cookie = {'visit_month': 'May'}
    pet_store_pet = '/pet'
    pet_store_upload = '/uploadImage'
    # get access token from user at run time

    def __init__(self, token):  # default constructor
        self.head_authorize = {'Authorization': 'Bearer {}'.format(token)}

    def get_auth_token(self):
        return self.head_authorize

