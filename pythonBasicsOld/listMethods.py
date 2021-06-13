# append() method

avg = []

avg.append('Steve')
avg.append('Tony')
print('Appended elements(values) in the list\n',avg)

# extend menthod

avg2 = ['Banner','Thor']
avg.extend(avg2)
print(avg)
print(avg2)

# extend via a string
list1 = ['a','e','i']
vow = "ou"
list1.extend(vow)
print("Vowels are ",list1)

# extend via a tuple.

team = ('Romanoff','clint')
avg.extend(team)
print('after extending by a tuple', avg)

# appending a list using another list as argument
vowels = ['a','e','i']
vo = ['o','u']
vowels.append(vo)
print(vowels)

# count() method

list1 = ["a","c","b","c","a","h","l", 1, 2, 3, 4]
print(list1.count ("a"))
print(list1.count ("h"))
print(list1.count ('o'))

# index()

os = ['kali', 'Ubuntu', 'debian', 'RHEL', 'Centos']
print(os.index('debian'))
os.append('kali')
print(os)
print(os.index('kali'))

# insert()

avgr = ['Tony','Banner','Thor']
avgr.insert(0,'Steve')
print(avgr)
avgr.insert(4,'Natasha')
print(avgr)

#remove ()
av = ['Tony','Steve','Loki','Thor']
av.remove("Loki")
print(av)
#av.remove('cap') for testing value error

num = [1,2,3,4,5,6,4,1,7]
num.remove(1)
print(num)

# pop ()
got = ["Tyrion","Sansa", "Arya","Joffrey","Ned-Stark"]

print(got.pop())
print(got.pop())
print(got)
print(got.pop(0))
print(got)


# sort ()
list1 = [5, 6, 7, 1, 4, 2, 0, 4, 2, 8]
list1.sort()
print("Sorted list1",list1)
list2 = [5, 6, 7, 1, 4, 2, 0, 4, 2, 8]
list2.sort(reverse=True)
print("Sorted list2",list2)

# sorting along with string as item in list : not supported in Python3

#list3 = [8, 7,4,2,1, "1", "a","@#", "nm"]
#list3.sort()
#print("Sorted list3",list3)

#list4 = [8, 7,4,2,1, "1", "a","@#", "nm"]
#list4.sort(reverse=True)
#print("Sorted list4",list4)

# complex eg list having tuple as items and sorting with key in argument
tupLst = [('a',4),('b',1),('v',5),('f',2)]
def sortWithKey(x):
    return x[1]
print('original List',tupLst)
tupLst.sort(key = sortWithKey)
print('Sorted list with help of key',tupLst)

# cmp argument in sort() method {not supported in python3}

# list6 = [10,9,3,7,2,1,23,1,561,1,1,96,1]
# def cmp1(x,y):
#  return
# list6.sort(cmp = cmp1)
# print(list6)



#  we want ascending order sort, but we also want to push all the 1s to the right {cmp not supported in Pythin 3  }:

# list5 = [10,9,3,7,2,1,23,1,561,1,1,96,1]
# def cmp1(x,y):
#  if x == 1 or y==1:
#      c = y-x
#  else:
#      c = x-y
#  return c
#
# list5.sort(cmp = cmp1)
# print(list5)

# reverse() mentod in list

avn = ['hulk', 'iron-man', 'Captain-America', 'Thor', 'vision', 'Clint']

avn.reverse()
print(avn)
