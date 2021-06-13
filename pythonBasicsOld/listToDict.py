# Make a dictionary from two lists. Both the lists are of equal length.
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c","d", "e"]
dict1 = {}
# checking length of lists.
if len(list1) == len(list2):
     lengthOfBothLists = len(list1)
     print('Length of both list is equal i.e. : ', lengthOfBothLists)
     for index1 in range(lengthOfBothLists):
         #print(list1[index1])
         #print(list2[index1])
         dict1[list1[index1]] = list2[index1] # its like adding an item to an empty list, dict1[index] = 'value'
     print(dict1)

     # one linear method using zip() function
     dict2 = dict([k for k in zip(list1, list2)])
     print(dict2)
