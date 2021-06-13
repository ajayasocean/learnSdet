# update() method test.

dict1 = {1:'Ajay', 2:'Sagar'}
dict2 = {3:'Learn', 4:'Python'}
dict1.update(dict2)
print('Updated dict1', dict1)

# dicts with same keys, d2 keys replaces d1 keys and values.
dict3 = {1:'Ajay', 2:'Sagar'}
dict4 = {2:'Learn', 4:'Python'}
dict3.update(dict4)
print('Updated dict3', dict3)
