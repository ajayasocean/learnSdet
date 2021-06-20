from config.configurations import *
# setting up a my sql connection with db
# connection = mysql.connector.connect(host='localhost', database='APIDevelop', user='ajay', password='Ocean#4321')
# print(connection.is_connected())
connection = get_connection()
# setting up a stream line with database to read and write from mysql db
cursor = connection.cursor()
# executing a select query. Note: don't use semicolon to end the query
cursor.execute('select sum(Amount) from CustomerInfo')
# fetching data from streamline
output_data = cursor.fetchall()  # fetching all rows from table.
print(output_data)  # printing output

# other way to fetch sum of Amount column
cursor.execute('select * from CustomerInfo')
all_rows = cursor.fetchall()
total = 0
for row in all_rows:
    total = total + row[2]
print('Sum of Amount is:\t', total)

# using update query
query = "update CustomerInfo set Location = %s where CourseName = %s"
# %s here indicates that value of column will be supplied externally.
data = ('US', 'WebServices')  # supplying value to %s in query
cursor.execute(query, data)
connection.commit()
# checking status of update query
cursor.execute("select * from CustomerInfo where CourseName = 'WebServices'")
update_result = cursor.fetchall()
print(update_result)

# insert query
insert_query = "INSERT INTO CustomerInfo VALUES (%s, %s, %s, %s)"
# %s here indicates that value of column will be supplied externally.
insert_data = ('Testing', '2021-06-20', 99, 'UK')
# supplying value to %s in query
print(cursor.execute(insert_query, insert_data))
connection.commit()
# checking status of insert query
cursor.execute("select * from CustomerInfo")
insert_result = cursor.fetchall()
print(insert_result)
# using delete query
del_query = "delete from CustomerInfo where CourseName = %s"
# %s here indicates that value of column will be supplied externally.
del_data = ("Testing",)  # supplying value to %s in query
cursor.execute(del_query, del_data)
connection.commit()
# checking status of delete query
cursor.execute("select * from CustomerInfo")
del_result = cursor.fetchall()
print(del_result)

# closing connection, if not done then db server will face latency
connection.close()
