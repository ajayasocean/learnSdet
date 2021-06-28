import csv

file = 'LoanApp.csv'
input_name = 'Test Vm'
input_status = 'Success'
with open(file, 'a') as add_csv:
    write_to_csv = csv.writer(add_csv)
    write_to_csv.writerow([input_name, input_status])


