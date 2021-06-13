# Find the number of ways to find whether a key exists in a dictionary or not.
dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(type(dict1))
inputKey = eval(input('Please enter key to find: \t'))
print(type(inputKey))
lengthOfDict1 = len(dict1)
ListofKeys = []
print('Length of given dictionay is: ', lengthOfDict1)
#print (dict1.has_key(1))   #not supported in Python3
# using if in control statement
if inputKey in dict1:
    print(inputKey,' key is present in given dictionary and its value is: ', dict1[inputKey])
else:
    print(inputKey,' key is not present in given dictionary.')


# another way using keys() method
if inputKey in dict1.keys():
    print(inputKey,' key is present in given dictionary and its value is: ', dict1[inputKey])
else:
    print(inputKey,' key is not present in given dictionary.')
