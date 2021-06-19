# defining api resources
class ApiResources:
    addBook = '/Library/Addbook.php'
    delBook = '/Library/DeleteBook.php'
    getBookByAuthorName = '/Library/GetBook.php'
    gitHubRepo = '/orgs/octokit/repos'
    HeadAccept = {'Accept': 'application/vnd.github.v3+json'}
    # get access token from user at run time

    def __init__(self, token):  # default constructor
        self.head_authorize = {'Authorization': 'Bearer {}'.format(token)}

    def get_auth_token(self):
        return self.head_authorize

