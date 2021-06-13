# Python's built-in functions for lists.

# len()

avg = ['Tony','Banner','Steve']
print("Length of avg list = ",len(avg))


# max()
list1 = [1,2,3,4,510]
print(max(list1))
list1 = [1,2,3,4,510,510.0]
print(max(list1))
list1 = [1,2,3,4,510.0,510]
print(max(list1))

list2 = ['a', '1']
print(max(list2))

#min()
list1 = [1,2,3,4,510]
print(min(list1))
list1 = [1,2,3,4,510, 1.0]
print(min(list1))
list1 = [1.0,1,2,3,4,510]
print(min(list1))

list2 = ['a', '1']
print(min(list2))

# list()
tup1 = ['A','j','a','y']
print(list(tup1))
name = "Ajay Sagar"
print(list(name))

#sorted() function

list3 = [2, 3, 0, 3, 1, 4, 7, 1]
print('list3 for sort',list3)
sortedList3 = sorted(list3)
print('sorted list 3 is\n',sortedList3, 'and is of type', type(sortedList3))

tup2 = ('b','c','d','e','a')
print('tuple for sort',tup2)
sortedTup2 = sorted(tup2)
print('sorted tuple  is\n',sortedTup2, 'and is of type', type(sortedTup2))
