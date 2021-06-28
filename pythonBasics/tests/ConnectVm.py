"""
This is a demo program to use paramiko to connect to virtual machine
"""
import paramiko as paramiko
import csv
import time

from config.configurations import get_config

# connecting to vm
host = get_config()['vm']['host']
port = get_config()['vm']['port']
username = get_config()['vm']['username']
password = get_config()['vm']['password']
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# Run commands on vm
stdin, stdout, stderr = ssh.exec_command('ls -la')
output1 = stdout.readlines()
for line1 in output1:
    print(line1)

# accessing a file data from
stdin, stdout, stderr = ssh.exec_command('cat vm_test_text')
output2 = stdout.readlines()
for line2 in output2:
    print(line2)


# upload file from local to vm
def upload_file(local, destination):
    source_path = local
    destination_path = destination
    sftp = ssh.open_sftp()
    sftp.put(source_path, destination_path)  # copying file from local to vm
    sftp.close()


local = "../config/LoanApp.csv"
destination = "LoanApp.csv"
upload_file(local, destination)

local = "../tests/WriteToCsv.py"
destination = "WriteToCsv.py"
upload_file(local, destination)


# Trigger the Bath Commands
stdin, stdout, stderr = ssh.exec_command('python3 WriteToCsv.py')

time.sleep(10)
# downloading and reading output csv.
sftp_download = ssh.open_sftp()
sftp_download.get('vm_test_text', '../output/vm_test_text.txt')
sftp_download.get('LoanApp.csv', '../output/LoanAppOut.csv')
sftp_download.close()
ssh.close()

output_file = '../output/LoanAppOut.csv'

with open(output_file, 'r') as read_csv_after_adding:
    csv_data_after_adding = csv.reader(read_csv_after_adding, delimiter=',')
    list_csv_data_after_adding = list(csv_data_after_adding)
    print(list_csv_data_after_adding)
