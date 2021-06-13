# user defined function

# user userInput
firstNumber = eval(input('Please enter first number for addition:\n'))
secondNumber = eval(input('Please enter second number for addition:\n'))
def addition (num1,num2):
    return (num1+num2)
result = addition(firstNumber,secondNumber)
print('Addtion result is = ',result)

# built-in functions
print(type(result))
print(id(result))
