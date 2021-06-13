# dictionary methods

# copy() method
avng1 ={'iron-man':'Tony', 'Cap':'Steve','BW':'Natasha'}

avng2 = avng1.copy()

print('copy of aveng1 is',avng2)

# Understanding copy vs assigment
a1 = {'iron-man':"Tony", "CA":"Steve","BW":"Natasha"}
a2 = a1
print(a2)
cw = a1.copy()
print(cw)
print('id of a1',id(a1))
print('id of a2',id(a2))
print('id of cw',id(cw))

print(a1)
a1['hulk']='Bruce-Banner'
print(a1)
print(a2)
print(cw)
##print(cw['hulk'])

# get() method

print('get having a default message',a1.get('iron-man',"not found"))
print(a1.get('panther',"not found"))
print('get having no default message', a1.get('black'))

# setdefault(); syntax: dict.setdefault(key1, default=None)
print('Current dict a1', a1)
print('New item', a1.setdefault('hulk', 'Unknown'))
print('Current dict a1', a1)
print('Another item', a1.setdefault('strange', 'unknow'))
print('Current dict a1', a1)
print('one more item', a1.setdefault('panther'))
print('Current dict a1', a1)
