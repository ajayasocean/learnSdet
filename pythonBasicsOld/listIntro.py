# introduction to lists

#empty lists
list1 = []

# list with values

avengers = ['Tony',"Steve",'Banner','Thor']

# unpacking a list

a,b = [1,2]
c,d,e,f = avengers
print(a)
print(b)
print(c)
print(d)
print(e)

# error unpacking
#x,y,z = [1,2]

# Accessing list values

print(avengers[1])
print(avengers[0])
print(avengers[-1])

# out of range index error
#print(avengers[3])

# slicing the list

print(avengers[1:3])
print(avengers[:4])
print(avengers[:])
print(avengers[2:])

list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(list2[2:13:2])


# Updating a list

print(avengers)
avengers[1] = 'Cap'
print(avengers)

#print("".join(avengers))

# Deleting values from a list
cwTeam =['Tony',"Steve",'Banner','Thor','Wanda']
#count (CWTeam)
del cwTeam[2]
print('after deleting index 2',cwTeam)
del cwTeam[2:3]
print("Shortened civil war team",cwTeam)

# addtion of python lists

avg1 = ['Tony',"Steve",'Banner','Thor']
avg2 = ['Hawk Eye','Romanoff']
print('Addition avg1+2',avg1+avg2)
print('Addition avg2+1',avg2+avg1)

# multiplying a python list
av = ['Hawk Eye','Romanoff']
print('address of list original value',id(av[0]))
print('address of multiplied value and not stored value',id(av[0]*3))
newAv = av*3
print(newAv)
print(id(newAv[1]))
print(id(newAv[3]))
print(id(newAv[5]))



# usig in operator:

if 'Romanoff' in av:
    print('Yes, Romanoff is in av')

if 'Tony' not in av:
    print('no tony is not in av')
