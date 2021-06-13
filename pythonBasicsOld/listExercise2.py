#With the for loop, take the following list and sort it based on the sum of the values of the tuples of the list:

list1 = [(1,5),(9,0),(12,3),(5,4),(13,6),(1,1)]
print("The original list of tuple is ", list1)

# getting length of list of tuples
lst = len(list1)
# Bubble sort
for i in range(lst):
      for j in range(lst-i-1):
        if (list1[j][0]+list1[j][1]) > (list1[j+1][0]+list1[j+1][1]):
            list1[j], list1[j+1] = list1[j+1], list1[j]
# print output
print("\nSorted list of tupples ", list1)
