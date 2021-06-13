#comprehensions

# for loop to create a list containing elements as squares of another list's elements respectively..

list1 = [2,3,4,5,6]
list2 = []
for each in list1:
 list2.append(each*each)
print(list2)

# comprehensions method
print([each*each for each in list1])

# if statement  to acheive: Create a new list that would contain the square of the even numbers of a given list

list1 = [2,3,4,5,6]
list2 = []
for each in list1:
    if each%2== 0:
        list2.append(each*each)
print(list2)

# comprehensions method
print([each*each for each in list1 if each%2==0])
