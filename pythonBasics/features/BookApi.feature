# Created by ajay at 21/06/21
  # https://behave.readthedocs.io/en/stable/install.html
  # https://snapcraft.io/install/pycharm-professional/ubuntu
  # create a directory by name 'feature' and create a new feature file in it.
Feature: Verify if Books are added and deleted using library api.
  # We have two api, 'http://216.10.245.166/Library/Addbook.php' and /Library/DeleteBook.php'
  # We are going test both these apis using data file like we have add_book_payload function in payload.py

  Scenario: Verify Addbook api
    Given the book details which needs to be added to library
    When we execute the Addbook PostAPI method
    Then book is successfully added