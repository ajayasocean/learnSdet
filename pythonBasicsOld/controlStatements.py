# Control Statements

# if..else control statement:
userInput = input('Enter your id\t')
uthorizedUsers = {'001': 'Mr.Test', '007': 'Mr.Bond', '003':'Mr.Sagar'}
if userInput in uthorizedUsers.keys():
    print('Welcome ',uthorizedUsers[userInput])
else:
    print('Id is not authorized, please enter valid id,\n Thank You!')

# if..elif..else statement

if userInput in uthorizedUsers.keys() and userInput == '003':
    print('Welcome ',uthorizedUsers[userInput])
elif userInput in uthorizedUsers.keys():
    print('Welcome Member, \n Have a great day ahead.')
else:
    print('Id is not authorized, please enter valid id,\n Thank You!')
