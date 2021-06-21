# numeric, string, list covered in dataTypes.py
# Tuple
days = ('Monday', 'Tuesday')
print('{} {}'.format(days, type(days)))

# Dictionary
port = {80: 'http', 23: 'ftp', 'ssh': 23}
print(port[23])
print(port['ssh'])

# creating a dictionary at run time
dict1 = {}  # empty dictionary declaration
dict1['firstName'] = 'Ajay'
dict1['lastName'] = 'Sagar'
dict1['gender'] = 'Male'
print(dict1)
print(dict1['lastName'])
