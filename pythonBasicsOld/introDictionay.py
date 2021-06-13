# Introduction to dictionary datatype

test = {'a':1, 'b':2, 'c':3}
print('Test dictionary',test)
print('value at c is: ',test['c']) # formattted string cann't be used if key in dectionay is of string type

port = {80: "HTTP", 23 : "Telnet", 443 : "HTTPS"}
print(port)
print(port[80])
print(port[23])

#name error
#print(port[1])

#deleting an item

del port[23]
print('Port: ',port)

#deleting whole dictionary
#del port
#print('Port',port)

# updating value of a key
dict1 = {80: "HTTP", 23 : "SMTP", 443 : "HTTPS"}
print(dict1)
dict1 [23] = 'Telnet'
print(dict1)

# adding a new item
dict1 [110] = 'POP'
print(dict1)
