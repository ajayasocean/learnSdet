#String boolean methods

#endswith()
str2 = 'Ajay Sagar'
print(str2.endswith('ar'))
print(str2.endswith('ay'))
print(str2.endswith('ay',2,4))

#startswith()
print(str2.startswith('Aj'))
print(str2.startswith('Sa'))
print(str2.startswith('Sa',5,11))

str1 = "Life should be great rather than long"
print(str1.endswith("ng"))
print(str1.endswith("er"))
print(str1.endswith("er",0,27))

#startswith()

print(str1.startswith("Li"))
print(str1.startswith("be"))
print(str1.startswith("be",12,16))



#isalpha()

st1 = "Hello"
print(st1.isalpha())
st2 = "Hello 123"
print(st2.isalpha())
st3 = "Hello "
print(st3.isalpha())

#isalnum()

li1 = "Hello123"
print(li1.isalnum())
li2 = "Hell0123#"
print(li2.isalnum())

#isdigit()
s1 = "12345"
print(s1.isdigit())
s2 = "123R"
print(s2.isdigit())

# isspace()

sr1 = "Hello"
print(sr1.isspace())
sr2 = ""
print(sr2.isspace())


# istitle()

sr3 = "ajay sagar"
print(sr3.istitle())
sr4 = "Ajay Sagar"
print(sr4.istitle())

# islower()

sr5 = "mohit"
print(sr5.islower())
sr6 = "Mohit"
print(sr6.islower())
sr7 = "Ajay123"
print(sr7.islower())
sr8 = "ajay@123"
print(sr8.islower())

# isuper()
sr9 = "AJAY"
print(sr9.isupper())
s1 = "Ajay"
print(s1.isupper())
s2 = "AJAY1234"
print(s2.isupper())
