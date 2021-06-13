#write a program to read an string as output from a file.
# concept is to open a file file to find matching string and print it.
#taking search string by user.
lineNumber = 0
listOfResults = []
userInput = input('Please enter your search string\n')
with open("/home/ajay/py/fileTORead.txt", 'r') as readFileObj:
    for line in readFileObj:
        lineNumber += 1
        if userInput in line:
            listOfResults.append((lineNumber, line.rstrip()))
            print('Found your string in file at \n',listOfResults)
