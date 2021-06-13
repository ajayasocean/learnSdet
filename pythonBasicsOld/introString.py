#introduction to strings in Python

str1 = "Hello Friday"
print (str1)
memAddress1 = id(str1)
print (memAddress1)

#ressignment

str1 = " Age Of Ultron"
print (str1)
memAddress2 = id(str1)
print (memAddress2)

#ctypes method to fetch value from memory address

import ctypes

val1 = ctypes.cast(memAddress2, ctypes.py_object).value
print (val1)

length1 = len (val1)
print (length1)

val2 = ""
length2 = len (val2)
print (length2)


#Subscript operator to access emements of a string

name = "The Avengers"
print (name)
print (name[0])
print (len(name))
print (name[11])
print (name[-1])
print (name[-12])

#Slicing for substrings

print ('slice 0:3',name [0:3])
print ('slice :6',name [:6])
print ('slice 4:',name [4:])
print ('slice 5:9',name [5:9])
print ('slice ::2',name [::2])

#Reversing a string

print ('reverse ::-1',name [::-1])
