# strings and its functions in python.
a = 'ajay_ocean'
str2 = 'Ocean'
print(a[1])  # j
print(a[0:4])  # slice
print(a+' Test')  # concat
print(str2 in a)  # True False (substring check)
# split and extract
split = str.split('.')
print(split)
print(split[0])

# striping
str3 = ' Ajay '
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())
