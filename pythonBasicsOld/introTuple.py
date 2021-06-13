# Indtroduction to tuples

tup1 = ()

tup2 = (1,2,3,4.5,"test",'a')

a = 1,2,3,4

print(tup1)
print(tup2)
print(a)
print(type(a))

avengers = ("Iron Man","Black Widow","Hawk Eye","Thor")
print(avengers[0])
print(avengers[3])
print(avengers[-2])
print(avengers[-3])

# slicing tuple

print(avengers[1:3])
print(avengers[:3])
print(avengers[1:])
print(avengers[5:6])
print(avengers[-3:-2])

# unpacking tuple
tup1 = (1,2,3)
x,y,z = tup1
print(x,y,z)
