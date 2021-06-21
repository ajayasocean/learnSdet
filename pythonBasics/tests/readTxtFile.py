# reading a text file using python
file = open('../config/testTextFile.txt')  # open(fileName is a function to read a text file.)
str_file_data = file.read()
print(str_file_data)
print(type(str_file_data))
print(file.read())  # read whole file
print(file.read(5))  # reading only limited data file.read(number of characters)
print(file.readline())  # read one line at a time
print(file.readline())  # read one line at a time

file.close()
