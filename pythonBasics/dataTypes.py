# data types:

a, b, c, d = 3, 4.5, 'Test', ' concat string '
# int
print('{} {} {} {}'.format('Type of ', a, ' is ', type(a)))
# float
print('{} {} {} {}'.format('Type of ', b, ' is ', type(b)))
# string
e = c+d
print(c+d)  # + can be used as both c and d are of string data type
print('type of e is ', type(e))

# list
# It is more or less like array list in java.
values = [1, 2, 4.5, 'statement']
print(values[3])  # positive index
print(values[-2])  # negative index
print(values[1:3])  # slicing
values.insert(3, 'Test')  # list.insert(index, element)
print(values)
values.append('End')  # list.append(new_element)
print(values)
values[2] = 3  # list[index] = updated_element)
print(values)
del values[5]  # del list[index] , deletes an element
print(values)
