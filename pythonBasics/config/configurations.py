"""
configurations here
"""
import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read('../config/globalProperties.ini')
    return config


connect_config = {'host': get_config()['sql']['host'],
                  'database': get_config()['sql']['database_name'],
                  'user': get_config()['sql']['username'],
                  'password': get_config()['sql']['password'],
                  }

print(connect_config)


def get_connection():
    # setting up a my sql connection with db
    try:
        print(connect_config)
        connection = mysql.connector.connect(**connect_config)
        print(connection)
        if connection.is_connected():
            print('connected successfully\n')
            return connection
    except Error as err:
        print(err)


# making a connection to database and executing add_book_query using get_query function
def get_query(add_book_query):
    add_book_connection = get_connection()
    add_book_cursor = add_book_connection.cursor()
    add_book_cursor.execute(add_book_query)
    result_set_data = add_book_cursor.fetchone()
    print(result_set_data)
    add_book_connection.close()
    return result_set_data
