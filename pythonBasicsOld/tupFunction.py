# Tuple functions

# len()

t1 = ('C',"Python","java","html")
print(len(t1))

# max()

t2 = (1,2,45,420)
print(max(t2))

t3 = (1,2,45.0,45)
print(max(t3))

t4 = (3,2,45,45.0)
print(max(t4))

t5 = ('800',"1")
print(max(t5))

t6 = ('aa',"z","az")
print(max(t6))

t7 = ('aa',"z","az","za")
print(max(t7))

#min()
print(min(t2))

print(min(t6))

# convert string to Tuple

str1 = "Ajay"
print(tuple(str1))

list1 = [1, 2, 3, 4, 5]
print(tuple(list1))

# deleting a Tuple
tup1 = (1,2,4)
print(tup1)
#del tup1
#print(tup1)

#sorted() fuction:

tup2 = (2,4,3,1)
print('sorted tuple', sorted(tup2))
print(sorted((5,9,7,8,6)))
