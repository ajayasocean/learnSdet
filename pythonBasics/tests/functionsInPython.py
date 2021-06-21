# Functions in python.
# Function declaration


def greet_me():  # function call
    print("Good Morning")


greet_me()


# function with argument

def gesture_good(name):
    print('Good Morning ', name)


gesture_good('Ajay')


def addition(a, b):
    return a+b


total = addition(5, 3)
print('Sum is = ', addition(5, 3))
print('{}{}'.format('Total = ', total))
