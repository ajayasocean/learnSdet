# strings and its functions in python.
str = 'ajay.sagar'
str2 = 'Sagar'
print(str[1])  # j
print(str[0:4]) # slice
print(str+' Test')  # concatination
print(str2 in str)  # True False (substring check)
# split and extract
splitted = str.split('.')
print(splitted)
print(splitted[0])

# striping
str3 = ' Ajay '
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())


