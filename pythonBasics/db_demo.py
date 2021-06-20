# deb demo
# pip install mysql-connector-python
import mysql.connector
# host, database_name, username, password
# setting up a mysql connection
con1 = mysql.connector.connect(host='localhost', user='ajay', password='Ocean#4321')
print(con1.is_connected())
# setting up a my sql connection with db
con2 = mysql.connector.connect(host='localhost', database='APIDevelop', user='ajay', password='Ocean#4321')
print(con2.is_connected())
# setting up a stream line with database to read and write from mysql db
cursor = con2.cursor()
# executing a select query. Note: don't use semicolon to end the query
cursor.execute('select * from CustomerInfo')
# fetching data from streamline
row_one = cursor.fetchone()  # first row from table (CustomerInfo)
print(row_one)  # output is a tuple (one row from table is in tuple datatype).
print(row_one[3])  # accessing and printing value at location column(via a index) from the row.
row_all = cursor.fetchall()  # fetching all rows from table.
print(row_all)  # output is a list of tuples (all rows from table as a list).
print(row_all[0])  # accessing and printing first row data.
print(row_all[0][0])  # accessing and printing value at courseName column(via a index) from the list of rows.
# Please Note: cursor() created a steam line hence fetching rows is per command.
# fetchone() fetches first row from steam line and cursor is set at 1st row.
# then if we fetch again the cursor returns remaining row or rows.

# closing connection, if not done then db server will face latency
con1.close()
con2.close()
