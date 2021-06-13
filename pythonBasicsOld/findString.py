# Use of find() method to find occurance of a substring in a given substring

str1 = "peace begins with a smile"
print(str1)
index = str1.find("with")
print ('with stand at ', index)

#multiple occurance

str2 = "What we think, we become"
index1 = str2.find("we")
print('we stands at', index1)

#rfind method to find substring from right hand side of the substring

index2 = str2.rfind("we")
print('we stands at', index2)
