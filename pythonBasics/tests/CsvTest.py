# Program to learn csv reading and writing with csv package.
import csv

file = '../config/LoanApp.csv'
name = []
status = []
loan_status = {}
with open(file, 'r') as read_csv:
    csv_data = csv.reader(read_csv, delimiter=',')
    print(csv_data)  # csv reader object
    list_csv_data = list(csv_data)  # converted csv reader object into list that returns list of list.
    print(list_csv_data)
    for each_row in list_csv_data:
        print(each_row)
        name.append(each_row[0])  # adding names to one list
        status.append(each_row[1])  # adding status to another list
        loan_status[each_row[0]] = each_row[1]  # setting names and status as dictionary,syntax: dict[key] = value
    print('Name:\n', name)
    print('Statuses:\n', status)
    print('As dictionary:\n', loan_status)
    # to access and find status against a name we have to options
    # 1. since we had only 2 columns, we used created a dictionary hence we can print result
    # If we want to print load status of Tom
    print("Tom's your loan status is: \t", loan_status['Tom'])
    # 2. we can use list manipulation
    needed_index = name.index('Tom')
    print("Tom's your loan status is: \t", status[needed_index])

# Now we want to add new rows to out csv by taking input from user.
input_name = input('Please enter name to add:')
input_status = input('Please enter status to add:')
with open(file, 'a') as add_csv:  # we can't use 'w' here as it will scrap the csv and write freshly.
    write_to_csv = csv.writer(add_csv)
    write_to_csv.writerow([input_name, input_status])

with open(file, 'r') as read_csv_after_adding:
    csv_data_after_adding = csv.reader(read_csv_after_adding, delimiter=',')
    list_csv_data_after_adding = list(csv_data_after_adding)
    print(list_csv_data_after_adding)

