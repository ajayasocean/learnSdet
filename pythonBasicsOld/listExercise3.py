#Use the list, [1,2,4,5,1,1,4,1,56], and find the index of all the 1 elements.

inputList = [1,2,4,5,1,1,4,1,56]
length = len(inputList)
list2 = []
for i in range(length):
     if inputList[i] == 1:
          list2.append(i)
print(list2)
# Excercise 4: above task by compehension
print([i for i in range(length) if inputList[i]==1])





# indexOfOnes = []
# for each in inputList:
#     if each == 1:
#         indexOfOnes.append(inputList.index(each))
#     print(indexOfOnes)
        #indexOfOnes.append(inputList.index(each))
        #print(inputList.index(each))
#print("indexs Of Ones in given list",indexOfOnes)
