# Exercise 1: Get the string "avengers" . from given list.
list1 = ["abc",[2,3,("mohit","the avengers")],1,2,3]
lengthOflist1 = len(list1)
print('Length of given list is', lengthOflist1)
a = list1[1]
print('Item at index 1', a)
lengthOfa = len(a)
print('Length of a is', lengthOfa)
b = a[2]
print(b,'is of type', type(b))
c = ''.join(b)
print(c,'is of type', type(c))
lengthofc = len(c)
print(c[9:])


# Exercise 2: With the for loop, take the following list
#and sort it based on the sum of the values of the tuples of the list:

list2 = [(1,5),(9,0),(12,3),(5,4),(13,6),(1,1)]
lengthOflist2 = len(list2)


# Use the list, [1,2,4,5,1,1,4,1,56] , and find the index of all the 1 elements.
list3 = [1,2,4,5,1,1,4,1,56]
for each in list3:
    if list[each] == 1:
        print('index of 1 = ', list[each])
