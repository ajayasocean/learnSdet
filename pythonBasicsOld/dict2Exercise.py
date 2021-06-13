#Use the dictionary port1  and make a new dictionary in which keys become values and values become keys.
port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}

# using zip() function
#keyList = []
#valueList = []
keysList = list(port1.keys())
print(keysList,'\t',type(keysList))
valuesList = list(port1.values())
print(valuesList, '\t', type(valuesList))
port2 = dict([k for k in zip(valuesList,keysList)])
print('old dicttionary: ',port1)
print('New dictionary(keys, values interchanged', port2)
