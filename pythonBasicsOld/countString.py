#count method to count characters or substrings in given strings

str1 = 'The Avengers'
length = len(str1)
print("Length of string is ",length)

#Find occurance of e in complete string
occ1 = str1.count("e")
print(occ1)

#Find occurance of e in specific substring
occ2 = str1.count("e",5,12)
print(occ2)
