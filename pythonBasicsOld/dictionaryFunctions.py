# Dictionary functions

# 1. Find lenght of a Dictionary

port = {80: "HTTP", 23 : "Telnet", 443 : "HTTPS"}
print(port)
print(type(port))

print('Length of dict = ',len(port))

# convert dictionary to string

test = str(port)
print(test)
print(type(test))


# Find max from a dictionary

dict1 = {1:'abc', 5:'hj', 43:'Dhoni', 100:'game', -1:56}
most = max(dict1)
print('most = ',most)
print(dict1[most])

# min in dictionary
least = min(dict1)
print('least = ',least)
print(dict1[least])

# second example max

dict2 = {'abc':1, 'hj':5, 'Dhoni':43, 'game':100, 'ab':-1}
m1 = max(dict2)
print('m1 = ', m1)
print(dict2[m1])

# second example min
l1 = min(dict2)
print('l1 =', l1)
print(dict2[l1])

#Example 3 for min and max from a dict

dict3 = {1:('a','b','cd'), 2:[1,10,100], 4:'test it on now'}

#max
m2 = max(dict3)
print('m2 = ', m2)
print(dict3[m2])

# min
l2 = min(dict3)
print('l2 =', l2)
print(dict3[l2])
