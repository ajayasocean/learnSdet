#String Justify methods

str1 = "Ajay Sagar"

str2= "Bhaskar Narayan Das"

print(str1.ljust(15,"#"))
print(str2.ljust(15,"#"))
print(str1.rjust(15,"#"))
print(str1.center(16,"#"))

#Justify strings(numbers) with zero

accNum = "54321"
binaryNum = "101010101"
print(accNum.rjust(16,"0"))
print(accNum.zfill(16))
print(binaryNum.rjust(16,"0"))
print(binaryNum.zfill(16))

# replace method
str3= "time is great and time is money"
print(str3.replace("is", "was"))
print(str3)
#print(str3.replace("is",1))
print(str3.replace("is", "was", 1))

# join method

name = ["Sagar","Ajay"]
print(" ".join(name))
print("".join(name))
print(",".join(name))
print("-".join(name))
